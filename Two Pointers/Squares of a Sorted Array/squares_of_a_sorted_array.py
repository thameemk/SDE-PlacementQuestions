#  Project : SDE Placement Questions
#  Filename : squares_of_a_sorted_array.py
#  Author : thameem
#  Created  time : Wed, 5 Jan 2022 at 11:46 PM India Standard Time
#  Last modified time : Wed, 5 Jan 2022 at 11:46 PM India Standard Time
from beartype import beartype


class SquaresOfASortedArray:
    @beartype
    def __init__(self: 'SquaresOfASortedArray', nums: list[int]) -> None:
        # conventional method
        for index, num in enumerate(nums):
            nums[index] = num * num
        nums.sort()
        self.result = nums


if __name__ == '__main__':
    res = SquaresOfASortedArray(nums=[-4, -1, 0, 3, 10])
    print(res.result)
