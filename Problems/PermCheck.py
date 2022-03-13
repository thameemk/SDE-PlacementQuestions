#  Project : SDE Placement Questions
#  Filename : PermCheck.py
#  Author : blacklist
#  Current modification time : Sun, 13 Mar 2022 at 11:41 PM India Standard Time
#  Last modified time : Sun, 13 Mar 2022 at 11:41 PM India Standard Time

class Solution:
    @staticmethod
    def perm_check(a: list[int]) -> int:
        a.sort()
        large_number = a[-1]
        if len(a) != large_number:
            return 0
        else:
            for i in range(1, large_number + 1):
                if i in a:
                    continue
                else:
                    return 0

            return 1


if __name__ == '__main__':
    print(Solution.perm_check(a=[4, 1, 3, 2]))

"""
Question: https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
"""
