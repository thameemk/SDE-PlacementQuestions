#  Project : SDE Placement Questions
#  Filename : contains_duplicate_ii.py
#  Author : thameem
#  Current modification time : Tue, 11 Oct 2022 at 11:07 pm India Standard Time
#  Last modified time : Tue, 11 Oct 2022 at 11:07 pm India Standard Time

from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    duplicate_values = {}

    for index, num in enumerate(nums):
        if num in duplicate_values and abs(index - duplicate_values[num]) <= k:
            return True
        else:
            duplicate_values[num] = index

    return False


if __name__ == '__main__':
    print(contains_nearby_duplicate(nums=[1, 2, 3, 1], k=3))
