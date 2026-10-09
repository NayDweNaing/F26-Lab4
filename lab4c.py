# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:
# Date:
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

def sum(a,b):
    return a+b

def main():
    num1 = int(input("Give me the first number: "));
    num2 = int(input("Give me the second number: "));
    add = sum(num1,num2)
    print("The sum is: ",add)
main()