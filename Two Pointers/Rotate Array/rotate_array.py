#  Project : SDE Placement Questions
#  Filename : rotate_array.py
#  Author : thameem
#  Created  time : Thu, 6 Jan 2022 at 12:00 AM India Standard Time
#  Last modified time : Thu, 6 Jan 2022 at 12:00 AM India Standard Time
from beartype import beartype


class RotateArray:
    @beartype
    def __init__(self: 'RotateArray', nums: list[int], k: int) -> None:
        for index, num in enumerate(nums):
            pass
        self.nums = nums


if __name__ == '__main__':
    response = RotateArray(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    print(response.nums)
