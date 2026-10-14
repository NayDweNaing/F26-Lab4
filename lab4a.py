# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 10/14/2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

list2 = [1,2,4,5,6,7]
list1 = [1,3,5,7,9,11]
def is_even(lista):
    even=False
    for i in lista:
        if i%2 == 0:
            even=True
            break
    return even  

print(is_even(list1))
print(is_even(list2))
