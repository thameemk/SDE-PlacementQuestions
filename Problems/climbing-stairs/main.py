"""
Link: https://leetcode.com/problems/climbing-stairs/
"""

def sum_of_fibonacci_series(num: int) -> int:
    sum = 0
    i = 1
    while i > num:
        sum = sum + i


def climbing_stairs(n: int) -> int:
    if n == 1:
        return 1

    fibonacci_series = [1, 1]

    for i in range(2, n+1):
        fibonacci_series.append(fibonacci_series[i-1]+fibonacci_series[i-2])    

    return fibonacci_series[-1]


if __name__ == '__main__':
    response = climbing_stairs(4)
    print(response)
