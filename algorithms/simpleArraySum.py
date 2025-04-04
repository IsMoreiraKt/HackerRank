"""
    Given an array of integers, find the sum of its elements.
    For example, if the array
        ar = [1, 2, 3]
        1 + 2 + 3 = 6, so return 6.

    Function Description
        Complete the simpleArraySum function with the following parameter(s):
            ar[n]: an array of integers

        Returns
            int: the sum of the array elements

    Input Format
        The first line contains an integer, n, denoting the size of the array.
        The second line contains n space-separated integers representing the array's elements.

    Constraints
        0 < n, ar[i]<=1000

    Sample Input
        STDIN
            6
            1 2 3 4 10 11
        FUNCTION
            ar[] size n = 6
            ar = [1, 2, 3, 4, 10, 11]

    Sample Output
        31

    Explanation
        Print the sum of the array's elements:
            1 + 2 + 3 + 4 + 10 + 11 = 31
"""

import math
import os
import random
import re
import sys

def simpleArraySum(ar: list) -> int:
    sum: int = 0

    for element in ar:
        sum += element

    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()

