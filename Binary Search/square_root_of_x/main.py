"""
Link: https://leetcode.com/problems/sqrtx/
"""
import math


def sqrt(x: int) -> int:
    return math.floor(math.sqrt(x))


def sqrt_conventional_method(x: int) -> int:
    sqrt_found = False
    sqrt = 1
    while(sqrt_found == False):
        current_square = sqrt*sqrt
        if current_square == x:
            sqrt_found = True
        elif current_square > x:
            sqrt_found = True
            sqrt = sqrt - 1
        else:
            sqrt = sqrt + 1

    return sqrt


if __name__ == '__main__':
    x = 8
    r1, r2 = sqrt(x), sqrt_conventional_method(x)
    print(r1, r2)
