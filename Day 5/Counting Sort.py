#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    n = max(arr)
    counter = [0] * (n +1)
    for i in arr:
        counter[i] += 1
   
    ans = []
    for i in range(len(counter)):
        for j in range(counter[i]):
            ans.append(i)
     
    return ans   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
