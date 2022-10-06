#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : thameem
#  Current modification time : Thu, 6 Oct 2022 at 10:27 pm India Standard Time
#  Last modified time : Thu, 6 Oct 2022 at 10:26 pm India Standard Time

"""
Link: https://leetcode.com/problems/majority-element/
Tags: Array, Hash Table, Divide & Conquer, Sorting, Counting
"""
from typing import List


def majority_element(nums: List[int]) -> int:
    set_nums = list(set(nums))

    len_of_array = len(nums)

    for num in set_nums:
        no_of_occurrence = nums.count(num)
        if no_of_occurrence > len_of_array/2:
            return num


if __name__ == '__main__':
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
