#  Project : SDE Placement Questions
#  Filename : 3_sum.py
#  Author : thameem
#  Current modification time : Mon, 15 May 2023 at 9:25 pm India Standard Time
#  Last modified time : Mon, 15 May 2023 at 9:25 pm India Standard Time
from beartype import beartype


# Link: https://leetcode.com/problems/3sum/


@beartype
def three_sum(nums: list[int]) -> list[tuple[int, int, int]]:
    len_of_array = len(nums)

    nums.sort()

    result = set()

    for i in range(len_of_array):
        left, right = i + 1, len_of_array - 1

        while left < right:

            sum_of_elements = nums[i] + nums[left] + nums[right]

            if sum_of_elements == 0:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1

            elif sum_of_elements < 0:
                left += 1
            else:
                right -= 1

    return list(result)


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
