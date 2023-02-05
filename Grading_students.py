#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

#-------------------- Below is the function I did
def gradingStudents(grades):
    for index in range(len(grades)):
        if int(grades[index]) < 38:
            grades[index] = grades[index]
        elif (math.ceil(int(grades[index]) / 5) * 5) - int(grades[index]) < 3:
            grades[index] = math.ceil(int(grades[index]) / 5) * 5
        else:
            grades[index] = grades[index]
    return(grades)
#-------------------
  
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
