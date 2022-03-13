#  Project : SDE Placement Questions
#  Filename : PermCheck.py
#  Author : blacklist
#  Current modification time : Sun, 13 Mar 2022 at 11:41 PM India Standard Time
#  Last modified time : Sun, 13 Mar 2022 at 11:41 PM India Standard Time

class Solution:
    @staticmethod
    def perm_check(a: list[int]) -> int:
        if len(a) != len(set(a)):
            return 0
        elif sum(a) == sum(range(1, len(a)+1)):
            return 1
        else:
            return 0


if __name__ == '__main__':
    print(Solution.perm_check(a=[4, 1, 3, 2]))

"""
Question: https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
"""
