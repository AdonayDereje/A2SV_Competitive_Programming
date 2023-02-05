#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    temp = 0
    count = 0
    for index1 in range(n):
        for index in range(n-1):
            if int(a[index]) > int(a[int(index + 1)]):
                temp = a[index]
                a[index] = a[index + 1]
                a[index + 1] = temp
                count += 1
                
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n - 1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
