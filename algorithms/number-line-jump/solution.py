#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    check = (max(x1, x2), max(v1, v2)) 
    if check == (x1, v1) or check == (x2, v2):
        print(check)
        return 'NO'
        
    flag_a = min(x1, x2)
    flag_b = max(x1, x2)
    
    for i in range(1, 10001):
        if flag_a > flag_b:
            print(f"x1: {x1}, v1: {v1}, x2: {x2}, v2: {v2}")
            return 'NO'
            
        if (v1 * i) + x1 == (v2 * i) + x2:
            print(f"x1: {x1}, v1: {v1}, x2: {x2}, v2: {v2}")
            return 'YES'
            
    return 'NO'
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
