"""
Link : https://leetcode.com/problems/plus-one/
"""


def plus_one(nums: list[int]) -> list[int]:
    larger_integer = int("".join(map(str, nums)))+1
    nums[:] = list(map(int,str(larger_integer)))
    return nums


if __name__ == '__main__':

    response = plus_one(nums=[1, 2, 3])

    print(response)
