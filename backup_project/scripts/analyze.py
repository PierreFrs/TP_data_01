#!/usr/bin/env python3

# Your Python code here
import sys

def analyze_file(filename):
    print(f"Analyzing {filename}")
    # Your analysis logic

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        print("No file provided")