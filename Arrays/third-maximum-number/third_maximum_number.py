#  Project : SDE Placement Questions
#  Filename : third_maximum_number.py
#  Author : thameem
#  Current modification time : Mon, 24 Oct 2022 at 8:28 pm India Standard Time
#  Last modified time : Mon, 24 Oct 2022 at 8:28 pm India Standard Time

def third_max(nums: list[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)

    if len(nums) >= 3:
        return nums[2]
    else:
        return nums[0]


if __name__ == '__main__':
    print(third_max([3, 2, 1]))
    print(third_max([2, 1]))
