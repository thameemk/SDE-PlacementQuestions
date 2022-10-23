#  Project : SDE Placement Questions
#  Filename : range_sum_query_immutable.py
#  Author : thameem
#  Current modification time : Sun, 23 Oct 2022 at 8:00 pm India Standard Time
#  Last modified time : Sun, 23 Oct 2022 at 8:00 pm India Standard Time
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        # _sum = 0
        # for i in range(left, right + 1):
        #     _sum = _sum + self.nums[i]
        # return _sum
        return sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sum_range(0, 2))
