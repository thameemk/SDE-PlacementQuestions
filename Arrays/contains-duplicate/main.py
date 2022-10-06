#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : thameem
#  Current modification time : Thu, 6 Oct 2022 at 10:42 pm India Standard Time
#  Last modified time : Thu, 6 Oct 2022 at 10:42 pm India Standard Time
"""
Link: https://leetcode.com/problems/contains-duplicate/
Tags: Array, Hash Table, Sorting
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(list(set(nums))) != len(nums)


if __name__ == '__main__':
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
