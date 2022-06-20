"""
Link: https://leetcode.com/problems/remove-element/
"""


from typing import List


def remove_element(nums: List[int], val: int) -> int:
    nums[:] = list(filter(lambda x: x != val, nums))
    return len(nums)


if __name__ == '__main__':
    response = remove_element(nums=[3, 2, 2, 3], val=3)
    print(response)
