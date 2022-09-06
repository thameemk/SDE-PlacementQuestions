#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Tue, 6 Sep 2022 at 12:50 am India Standard Time
#  Last modified time : Tue, 6 Sep 2022 at 12:50 am India Standard Time

"""
Link: https://leetcode.com/problems/pascals-triangle-ii/
"""
from typing import List


class Solution:

    @staticmethod
    def get_row(row_index: int) -> List[int]:

        # todo - return row itself without creating entire triangle

        pascals_triangle = [[1]]

        if row_index == 0:
            return pascals_triangle[0]

        for i in range(1, row_index + 1):

            pascals_triangle.append([1])

            for j in range(1, i):
                pascals_triangle[i].append(pascals_triangle[i -
                                                            1][j] + pascals_triangle[i - 1][j - 1])

            pascals_triangle[i].append(1)

        return pascals_triangle[row_index]
