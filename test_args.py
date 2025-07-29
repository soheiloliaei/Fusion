#!/usr/bin/env python3

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Test argument parsing")
    parser.add_argument("command", nargs="?", help="Command to execute")
    parser.add_argument("agent", nargs="?", help="Agent name (for run command)")
    parser.add_argument("input", nargs="*", help="Input prompt")
    
    print(f"sys.argv: {sys.argv}")
    args = parser.parse_args()
    print(f"args.command: {args.command}")
    print(f"args.agent: {args.agent}")
    print(f"args.input: {args.input}")
    
    input_text = " ".join(args.input) if args.input else ""
    print(f"input_text: '{input_text}'")

if __name__ == "__main__":
    main() 