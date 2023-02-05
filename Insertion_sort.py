#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    to_be_sorted = arr[n-1]
    temp = 0
    for index in range(n):
        if to_be_sorted < arr[n-index-2] and index != n-1:
            arr[n-index-1] = arr[n-index-2]
            print(*arr)
        else:
            arr[n-(index+1)] = to_be_sorted
            print(*arr)
            break
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
