#!/usr/bin/env python3
import sys
import argparse

def main():
    print("DEBUG: Starting simple fusion.py")
    print(f"sys.argv: {sys.argv}")
    
    parser = argparse.ArgumentParser(description="Simple Fusion v14 - Programmable Agent OS")
    parser.add_argument("command", nargs="?", help="Command to execute")
    parser.add_argument("agent", nargs="?", help="Agent name (for run command)")
    parser.add_argument("input", nargs="*", help="Input prompt")
    parser.add_argument("--config", default=".fusion.json", help="Configuration file path")
    
    args = parser.parse_args()
    print(f"DEBUG: After parse_args - command={args.command}, agent={args.agent}, input={args.input}")
    
    if not args.command or args.command == "help":
        print("Help command")
        return
        
    if args.command == "status":
        print("Status command")
        return
        
    # Handle input parsing correctly
    input_text = ""
    if args.command == "run":
        # For run command: command agent input
        if args.input:
            input_text = " ".join(args.input)
    elif args.command in ["pipeline", "pattern"]:
        # For pipeline/pattern commands: command input
        # The agent argument is actually the input for these commands
        if args.agent:
            input_text = args.agent
        if args.input:
            input_text += " " + " ".join(args.input)
    
    print(f"DEBUG: input_text='{input_text}'")
    
    if args.command == "run":
        if not args.agent or not input_text:
            print("❌ Error: 'run' command requires both agent and input")
            return
        print(f"✅ Run command with agent={args.agent}, input={input_text}")
        
    elif args.command == "pipeline":
        if not input_text:
            print("❌ Error: 'pipeline' command requires input")
            return
        print(f"✅ Pipeline command with input: {input_text}")
        
    elif args.command == "pattern":
        if not input_text:
            print("❌ Error: 'pattern' command requires input")
            return
        print(f"✅ Pattern command with input: {input_text}")
        
    else:
        print(f"❌ Unknown command: {args.command}")

if __name__ == "__main__":
    main() 