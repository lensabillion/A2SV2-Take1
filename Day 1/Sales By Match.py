#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = {}
    pair = 0
    for el in ar:
        if el not in count:
            count[el] = 0
        count[el] += 1
    for i in count:
        if count[i] >= 2:
            pair += count[i] // 2
    return pair
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
