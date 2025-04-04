"""
    Complete the function solveMeFirst to compute the sum of two integers.

    Example:
        a = 7
        b = 3
        Return 10.

    Function Description:
        Complete the solveMeFirst function with the following parameters:
            int a: the first value
            int b: the second value
        Returns:
            int: the sum of a and b
        Constraints:
            - int: the sum of a and b

        Sample Input:
            a = 2
            b = 3
        Sample Output:
            5
        Explanation:
            2 + 3 = 5
"""

def solveMeFirst(a: int, b: int):
    return a + b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)

