"""
  Staircase detail
  This is staircase of size n = 4.

     *
    **
   ***
  ****

  Its base and height are both equal to n.
  It is drawn using # symbols and spaces.
  The last line is not preceded by any spaces.
  Write a program that prints a staircase of size n.


  Function Description:
    Complete the staircase function with the following parameter(s):
      int n: an integer


  Print:
    Print a staircase as described above.
    No value should be returned.

    Note:
      The last line is not preceded by spaces.
      All line are right-aligned.


  Input Format:
    A single integer, n, denoting the size of the staircase.


  Constraints:
    0 < n <= 100


  Sample Input:
    6


  Sample Output:
         #
        ##
       ###
      ####
     #####
    ######


  Explanation:
    The staircase is right-aligned, composed of # symbols and spaces,
      and has a height and width of n = 6.
"""
import math
import os
import random
import re
import sys

def staircase(n: int):
  for i in range(n):
    spaces = n - (i + 1)
    print(" "*spaces, end="")
    print("#"*(i + 1))

if __name__ == '__main__':
  n = int(input().strip())
  staircase(n)
