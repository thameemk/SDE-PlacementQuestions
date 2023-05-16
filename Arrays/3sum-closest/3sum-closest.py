#  Project : SDE Placement Questions
#  Filename : 3sum-closest.py
#  Author : thameem
#  Current modification time : Tue, 16 May 2023 at 11:05 pm India Standard Time
#  Last modified time : Tue, 16 May 2023 at 11:05 pm India Standard Time

# Link: https://leetcode.com/problems/3sum-closest/

from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()

    n = len(nums)

    closest_sum = nums[0] + nums[1] + nums[2]

    for i in range(n):
        left, right = i + 1, n - 1

        while left < right:

            sum_of_current_elements = nums[i] + nums[left] + nums[right]

            if sum_of_current_elements == target:
                return sum_of_current_elements
            elif sum_of_current_elements < target:
                left += 1
            else:
                right -= 1

            if abs(closest_sum - target) > abs(sum_of_current_elements - target):
                closest_sum = sum_of_current_elements

    return closest_sum
