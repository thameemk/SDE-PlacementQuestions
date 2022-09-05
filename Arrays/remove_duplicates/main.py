"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


from typing import List


def remove_duplicates(numbers: List[int]) -> int:
    numbers[:] = sorted(set(numbers))
    return len(numbers)


if __name__ == '__main__':
    print(remove_duplicates(numbers=[1,1,2]))
