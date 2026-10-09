# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

list = [1,2,3,4,5,6,7,8];

def even_num(list):
    newlist = [];
    for i in list:
        if i%2 == 0:
            newlist.append(i);
    print(newlist)

even_num(list)
