#!/usr/bin/env python3
import sys
import argparse

def main():
    print("DEBUG: Starting test script")
    print(f"sys.argv: {sys.argv}")
    
    parser = argparse.ArgumentParser(description="Test Fusion v14 argument parsing")
    parser.add_argument("command", nargs="?", help="Command to execute")
    parser.add_argument("agent", nargs="?", help="Agent name (for run command)")
    parser.add_argument("input", nargs="*", help="Input prompt")
    
    args = parser.parse_args()
    print(f"DEBUG: After parse_args - command={args.command}, agent={args.agent}, input={args.input}")
    
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
    
    if args.command == "pipeline":
        if not input_text:
            print("❌ Error: 'pipeline' command requires input")
            return
        print(f"✅ Pipeline command with input: {input_text}")

if __name__ == "__main__":
    main() 