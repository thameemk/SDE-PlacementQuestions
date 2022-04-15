#  Project : SDE Placement Questions
#  Filename : SumOfZero.py
#  Author : blacklist
#  Current modification time : Thu, 14 Apr 2022 at 10:37 PM India Standard Time
#  Last modified time : Thu, 14 Apr 2022 at 10:37 PM India Standard Time

class SumOfZero:
    @staticmethod
    def check_sum(num_list: list[int]) -> bool:
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                if num_list[i] + num_list[j] == 0:
                    return True

        return False


"""
Problem: https://www.educative.io/courses/learn-python-3-from-scratch/qVAYRZK0AK7
"""

if __name__ == '__main__':
    print(SumOfZero.check_sum([10, -14, 26, 5, -3, 13, -5]))
