# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 14/10/2026
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

def compute(*, num1, num2, operator):
    if operator == "*":
        print("The answer is", num1 * num2)
    elif operator == "-":
        print("The answer is", num1 - num2)
    elif operator == "/":
        if num2 == 0:
            print("Error: can't divide by zero")
        else:
            print("The answer is", num1 / num2)
    elif operator == "+":
        print("The answer is", num1 + num2)
    else:
        print("Invalid operator:", operator)
 
def main():
    print("Usage: give me two numbers and one operator: * + - /")
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    c = input("Your Operator: ")
    compute(operator=c, num1=a, num2=b)
 
main()