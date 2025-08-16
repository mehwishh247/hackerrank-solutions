#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.

def flatlandSpaceStations(n, c):
    c.sort()
    
    if len(c) == n:
        return 0
        
    distances = []
    distances.append(abs(0 - c[0]))
    distances.append(abs((n-1) - c[-1]))
    
    for i in range(len(c) - 1):
        distances.append(abs(c[i] - c[i + 1]) // 2)
        
    return max(distances)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
