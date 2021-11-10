#  [Only For Educational Purpose]
#  Project : SDE-Placement Questions
#  Filename : two_sum.py
#  Author : thameem
#  Created  time : Thu, 11 Nov 2021 at 12:26 AM India Standard Time
#  Last modified time : Thu, 11 Nov 2021 at 12:24 AM India Standard Time

from beartype import beartype


class Solution:

    @staticmethod
    @beartype
    def two_sum(nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    index_of_first_num, index_of_second_num = Solution.two_sum(nums=[3, 2, 4], target=6)
    print(index_of_first_num, index_of_second_num)
