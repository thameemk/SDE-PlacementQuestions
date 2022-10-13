#  Project : SDE Placement Questions
#  Filename : move_zeroes.py
#  Author : thameem
#  Current modification time : Wed, 12 Oct 2022 at 10:27 pm India Standard Time
#  Last modified time : Wed, 12 Oct 2022 at 10:27 pm India Standard Time
from typing import List


def move_zeroes(nums: List[int]) -> None:
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(0)


if __name__ == '__main__':
    in_nums = [0, 1, 0, 3, 12]
    move_zeroes(in_nums)
    print(in_nums)
