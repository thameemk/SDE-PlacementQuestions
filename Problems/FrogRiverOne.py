#  Project : SDE Placement Questions
#  Filename : FrogRiverOne.py
#  Author : blacklist
#  Current modification time : Sun, 13 Mar 2022 at 11:27 PM India Standard Time
#  Last modified time : Sun, 13 Mar 2022 at 11:27 PM India Standard Time
class Solution:
    @staticmethod
    def frog_river_one(x: int, a: list[int]):
        if x > len(a):
            return -1
        else:
            hash_map = {}
            for index, value in enumerate(a):
                hash_map[value] = index
                if len(hash_map) == x:
                    return index

        return -1


if __name__ == '__main__':
    Solution.frog_river_one(x=5, a=[1, 3, 1, 4, 2, 3, 5, 4])

"""
Question: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
"""