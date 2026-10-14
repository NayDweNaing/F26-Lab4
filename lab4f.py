# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 14/10/2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.

def get_initials(*args):
    initials = []
    for name in args:       
        initials.append(name[0])
    return initials

def main():
    result = get_initials("Alice", "Bob", "Charlie", "David")
    print(result)

main()