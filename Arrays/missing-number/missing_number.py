#  Project : SDE Placement Questions
#  Filename : missing_number.py
#  Author : thameem
#  Current modification time : Wed, 12 Oct 2022 at 9:53 pm India Standard Time
#  Last modified time : Wed, 12 Oct 2022 at 9:53 pm India Standard Time
from typing import List


def missing_number(nums: List[int]) -> int:
    len_of_nums = len(nums)
    nums.sort()

    for i in range(0, len_of_nums):
        if not i == nums[i]:
            return i

    return len_of_nums


def missing_number_2(nums: List[int]) -> int:
    len_of_nums = len(nums)

    actual_sum = (len_of_nums * (len_of_nums + 1)) // 2

    given_sum = sum(nums)

    return actual_sum - given_sum


if __name__ == '__main__':
    print(missing_number(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missing_number_2(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
