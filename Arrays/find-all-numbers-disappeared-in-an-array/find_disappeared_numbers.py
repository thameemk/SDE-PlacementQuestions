

from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:

    return [i for i in range(1, len(nums)+1) if i not in nums]


if __name__ == '__main__':

    print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(find_disappeared_numbers([4, 3, 2, 7, 7, 2, 3, 1]))
    print(find_disappeared_numbers([1, 1]))
