import os
import tempfile
import json
from datetime import datetime
from typing import Dict, Any, Optional

class VoiceInput:
    def __init__(self):
        self.voice_log = []
        self.whisper_available = self._check_whisper_availability()
        self.fallback_available = self._check_fallback_availability()
    
    def _check_whisper_availability(self) -> bool:
        """Check if whisper package is available"""
        try:
            import whisper
            return True
        except ImportError:
            return False
    
    def _check_fallback_availability(self) -> bool:
        """Check if speech_recognition package is available"""
        try:
            import speech_recognition as sr
            return True
        except ImportError:
            return False
    
    def get_available_methods(self) -> Dict[str, bool]:
        """Get available voice input methods"""
        return {
            "whisper": self.whisper_available,
            "speech_recognition": self.fallback_available,
            "manual": True  # Always available
        }
    
    def record_voice_input(self, method: str = "auto", duration: int = 5) -> Optional[str]:
        """
        Record voice input and convert to text
        
        Args:
            method: "whisper", "speech_recognition", "manual", or "auto"
            duration: Recording duration in seconds
            
        Returns:
            Transcribed text or None if failed
        """
        if method == "auto":
            if self.whisper_available:
                method = "whisper"
            elif self.fallback_available:
                method = "speech_recognition"
            else:
                method = "manual"
        
        print(f"🎤 Voice Input Mode: {method}")
        
        if method == "whisper":
            return self._record_with_whisper(duration)
        elif method == "speech_recognition":
            return self._record_with_speech_recognition(duration)
        elif method == "manual":
            return self._manual_text_input()
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def _record_with_whisper(self, duration: int) -> Optional[str]:
        """Record and transcribe using Whisper"""
        try:
            import whisper
            import sounddevice as sd
            import soundfile as sf
            import numpy as np
            
            print(f"🎙️  Recording for {duration} seconds... (Whisper)")
            print("🔴 Recording started - speak now!")
            
            # Record audio
            sample_rate = 16000
            audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
            sd.wait()  # Wait until recording is finished
            
            print("⏹️  Recording stopped")
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                sf.write(temp_file.name, audio, sample_rate)
                temp_filename = temp_file.name
            
            # Load Whisper model and transcribe
            print("🧠 Transcribing with Whisper...")
            model = whisper.load_model("base")
            result = model.transcribe(temp_filename)
            
            # Clean up
            os.unlink(temp_filename)
            
            transcript = result["text"].strip()
            print(f"📝 Transcript: {transcript}")
            
            return transcript if transcript else None
            
        except ImportError:
            print("❌ Whisper not available. Install with: pip install openai-whisper sounddevice soundfile")
            return None
        except Exception as e:
            print(f"❌ Error with Whisper: {e}")
            return None
    
    def _record_with_speech_recognition(self, duration: int) -> Optional[str]:
        """Record and transcribe using speech_recognition"""
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            
            print(f"🎙️  Recording for {duration} seconds... (Speech Recognition)")
            print("🔴 Recording started - speak now!")
            
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=duration, phrase_time_limit=duration)
            
            print("⏹️  Recording stopped")
            print("🧠 Transcribing with Google Speech Recognition...")
            
            try:
                transcript = recognizer.recognize_google(audio)
                print(f"📝 Transcript: {transcript}")
                return transcript
            except sr.UnknownValueError:
                print("❌ Could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"❌ Error with speech recognition service: {e}")
                return None
                
        except ImportError:
            print("❌ speech_recognition not available. Install with: pip install SpeechRecognition pyaudio")
            return None
        except Exception as e:
            print(f"❌ Error with speech recognition: {e}")
            return None
    
    def _manual_text_input(self) -> Optional[str]:
        """Fallback to manual text input"""
        print("⌨️  Voice input not available - using manual text input")
        try:
            text = input("📝 Enter your text: ").strip()
            return text if text else None
        except KeyboardInterrupt:
            print("\n❌ Input cancelled")
            return None
    
    async def process_voice_input(self, agent_name: str, agent_map: Dict[str, Any], 
                                method: str = "auto", duration: int = 5, 
                                risk_threshold: float = 0.8) -> Dict[str, Any]:
        """
        Complete voice-to-agent workflow
        
        Args:
            agent_name: Name of the agent to run
            agent_map: Mapping of agent names to agent classes
            method: Voice input method
            duration: Recording duration
            risk_threshold: Threshold for high-risk utterances
            
        Returns:
            Dictionary with results
        """
        # Step 1: Record and transcribe voice
        transcript = self.record_voice_input(method, duration)
        
        if not transcript:
            return {
                "success": False,
                "error": "Failed to get voice input",
                "timestamp": datetime.now().isoformat()
            }
        
        # Step 2: Run through synthetic reasoning
        from fusion import risk_aware_agent_runner
        
        if agent_name not in agent_map:
            return {
                "success": False,
                "error": f"Agent '{agent_name}' not found",
                "transcript": transcript,
                "timestamp": datetime.now().isoformat()
            }
        
        agent_class = agent_map[agent_name]
        agent = agent_class()
        
        print(f"🤖 Processing with {agent_name}...")
        result = await risk_aware_agent_runner(transcript, agent, agent_name)
        
        # Step 3: Check for high-risk utterances
        risk_score = result.get("synthetic_meta", {}).get("risk_score", 0.0)
        high_risk = risk_score > risk_threshold
        
        if high_risk:
            print(f"🚨 HIGH RISK UTTERANCE DETECTED (risk: {risk_score:.2f})")
            confirmation = input("⚠️  Do you want to proceed? (y/N): ").strip().lower()
            if confirmation != 'y':
                print("❌ Processing cancelled due to high risk")
                return {
                    "success": False,
                    "error": "Cancelled due to high risk",
                    "transcript": transcript,
                    "risk_score": risk_score,
                    "timestamp": datetime.now().isoformat()
                }
        
        # Step 4: Create result summary
        voice_result = {
            "success": True,
            "transcript": transcript,
            "agent_name": agent_name,
            "method_used": method,
            "duration": duration,
            "risk_score": risk_score,
            "high_risk": high_risk,
            "synthetic_meta": result.get("synthetic_meta", {}),
            "agent_output": result.get("agent_output", {}),
            "routed": result.get("routed", False),
            "timestamp": datetime.now().isoformat()
        }
        
        # Log the session
        self.voice_log.append(voice_result)
        
        return voice_result
    
    def save_voice_log(self, filename: str = None) -> None:
        """Save voice session log to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"voice_session_log_{timestamp}.json"
        
        with open(filename, "w") as f:
            json.dump({
                "session_timestamp": datetime.now().isoformat(),
                "voice_sessions": len(self.voice_log),
                "available_methods": self.get_available_methods(),
                "session_results": self.voice_log
            }, f, indent=2)
        
        print(f"📁 Voice session log saved to: {filename}")
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Get summary of voice sessions"""
        if not self.voice_log:
            return {"total_sessions": 0, "success_rate": 0.0, "average_risk": 0.0}
        
        total_sessions = len(self.voice_log)
        successful_sessions = sum(1 for session in self.voice_log if session["success"])
        success_rate = successful_sessions / total_sessions
        
        risk_scores = [
            session.get("risk_score", 0.0) 
            for session in self.voice_log 
            if session["success"]
        ]
        average_risk = sum(risk_scores) / len(risk_scores) if risk_scores else 0.0
        
        high_risk_sessions = sum(
            1 for session in self.voice_log 
            if session.get("high_risk", False)
        )
        
        return {
            "total_sessions": total_sessions,
            "successful_sessions": successful_sessions,
            "success_rate": round(success_rate, 3),
            "average_risk": round(average_risk, 3),
            "high_risk_sessions": high_risk_sessions,
            "methods_used": list(set(
                session.get("method_used", "unknown") 
                for session in self.voice_log
            ))
        }

# Global voice input instance
voice_input = VoiceInput()

def get_voice_input() -> VoiceInput:
    """Get the global voice input instance"""
    return voice_input