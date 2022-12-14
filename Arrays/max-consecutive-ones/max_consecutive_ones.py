#  Project : SDE Placement Questions
#  Filename : max_consecutive_ones.py
#  Author : thameem
#  Current modification time : Wed, 14 Dec 2022 at 12:27 am India Standard Time
#  Last modified time : Wed, 14 Dec 2022 at 12:27 am India Standard Time
from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    max_consecutive = 0

    temp = 0

    for i in nums:
        if i == 1:
            temp += 1
        else:
            max_consecutive = max(temp, max_consecutive)
            temp = 0

    return max(temp, max_consecutive)


if __name__ == '__main__':
    print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
    print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
    print(find_max_consecutive_ones([0]))
