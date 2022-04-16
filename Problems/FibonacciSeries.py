#  Project : SDE Placement Questions
#  Filename : FibonacciSeries.py
#  Author : blacklist
#  Current modification time : Sat, 16 Apr 2022 at 11:50 PM India Standard Time
#  Last modified time : Sat, 16 Apr 2022 at 11:50 PM India Standard Time
class FibonacciSeries:
    @staticmethod
    def get_n_th_fibonacci_series_element(number: int) -> int:
        if number <= 0:
            return -1
        elif number == 1:
            return 0
        elif number == 2 or number == 3:
            return 1
        else:
            return FibonacciSeries.get_n_th_fibonacci_series_element(
                number - 1) + FibonacciSeries.get_n_th_fibonacci_series_element(number - 2)


"""
Problem: https://www.educative.io/courses/learn-python-3-from-scratch/7AgNXX6vKlQ
"""

if __name__ == '__main__':
    print(FibonacciSeries.get_n_th_fibonacci_series_element(number=7))
