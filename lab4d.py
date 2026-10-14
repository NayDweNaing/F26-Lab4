# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 14/10/2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.

def main():
    print("Usage, give me two numbers and one opeator: * + - / ")
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    c = input("Your Operator: " )
    compute(a,b,c);

def compute(a,b,c):
    if c == "*":
        print("The answer is", a*b);
    elif c == "-":
        print("The answer is", a-b);
    elif c == "/":
        if b == 0:
            print("Error: can't divide by zero");
        else:
            print("The answer is", a/b);
    elif c == "+":
        print("The answer is", a+b);
    else:
        print("The answer is", a+b);

main()