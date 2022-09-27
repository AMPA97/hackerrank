"""Link of the problem:
https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    pages_book_start=list((x+1 for x in range (0,n+1) if (((x+1)%2)!=0)))
    pages_book_fin=[x-1 for x in reversed(pages_book_start)]
    page_start=len([x for x in pages_book_start if x<p])
    page_fin=len([x for x in pages_book_fin if p<x])
    if page_start<page_fin or page_start==page_fin:
        #print(page_start)
       return page_start
    elif page_start>page_fin:
       #print(page_fin)
       return page_fin

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
