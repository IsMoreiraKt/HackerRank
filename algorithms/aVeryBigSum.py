"""
    In this challenge, you need to calculate and print the sum of elements in an array,
        considering that some integers may be very large.

    Function Description:
        Complete the aVeryBigSum function with the following parameter(s):
            int ar[n]: an array of integers

    Return:
        long: the sum of the array elements

    Input Format:
        The first line of the input consists of an integer n.
        The next line contains n space-separated contained in the array.

    Output Format:
        Return the integer sum of elements in the array.

    Constraints:
        1 <= n <= 10
        0 <= ar[i] <= 10 ** 10

    Sample Input:
        stdin
            5
            1000000001 1000000002 1000000003 1000000004 1000000005
        Function
            arr[] size n = 5
            arr[...]

    Output:
        5000000015

    Note:
        The range of 32-bit integer is
            (-2 ** 31) to (2 ** 31 - 1)
                or
            [-2147483648, 2147483647].

        When we add several integer values, the resulting sum might
            exceed the above range.
        Yout might need to use long int C/C++/Java to store such sums.
"""
import math
import os
import random
import re
import sys

def aVeryBigSum(ar: list) -> int:
    sum: int = 0

    for element in ar:
        sum += element

    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()

