"""
Link: https://leetcode.com/problems/maximum-subarray/
"""


def maximum_sub_array(nums: list[int]) -> int:
    temporary_sum = nums[0]
    actual_sum = nums[0]
    for i in range(1, len(nums)):
        if temporary_sum >= 0:
            temporary_sum = temporary_sum + nums[i]
        else:
            temporary_sum = nums[i]

        if actual_sum < temporary_sum:
            actual_sum = temporary_sum

    return actual_sum


if __name__ == '__main__':
    response = maximum_sub_array(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(response)
