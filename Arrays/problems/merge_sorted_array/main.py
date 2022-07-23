#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Sun, 24 Jul 2022 at 12:51 AM India Standard Time
#  Last modified time : Sun, 24 Jul 2022 at 12:51 AM India Standard Time

"""
Link: https://leetcode.com/problems/merge-sorted-array/
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1[:] = nums1[:m]
    nums1.extend(nums2[:n])
    nums1[:] = sorted(nums1)


if __name__ == '__main__':
    _nums1 = [1, 2, 3, 0, 0, 0]
    _m = 3
    _nums2 = [2, 5, 6]
    _n = 3
    merge(_nums1, _m, _nums2, _n)
