"""
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    For example, the square matrix arr is shown bellow:
        1 2 3
        4 5 6
        9 8 9
    The left-to-right diagonal = 1 + 5 + 9 = 15
    The right-to-left diagonal = 3 + 5 + 9 = 17

    Their absolute difference is | 15 - 17 | = 2

    Function Description:
        Complete the diagonalDifference function with the following parameter:
            int arr[n][m]: a 2-D array of integers

    Return:
        int: the absolute difference in sums along the diagonals

    Input Format:
        The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
        Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

    Sample Input:
        stdin
            3

            11 2 4
            4 5 6
            10 8 -12
        function
            arr[][] sizes n = 3, m = 3
            arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    Sample Output:
        15

    Explanation
        The primary diagonal is:
            11
             5
              -12
        Sum across the primary diagonal:
            11 + 5 - 12 = 4

        The secondary diagonal is:
              4
             5
            10
        Sum across the secondary diagonal:
            4 + 5 + 10 = 19

        Diference:
            | 4 - 19 | = 15
"""
import math
import os
import random
import re
import sys

def diagonalDifference(arr: list) -> int:
    left_sum: int = 0
    right_sum: int = 0

    for iterator, line in enumerate(arr):
        left_sum += line[iterator]
        right_sum += line[-iterator - 1]

    return abs(left_sum - right_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

