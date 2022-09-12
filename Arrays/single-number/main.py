"""
Link: https://leetcode.com/problems/single-number/
Topics: Array, Bit Manipulation 
"""

from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map:
                map[num] = map[num]+1
            else:
                map[num] = 1

        keys = list(map.keys())
        values = list(map.values())

        return keys[values.index(1)]


if __name__ == '__main__':
    print(Solution().single_number(nums=[2,2,1]))
