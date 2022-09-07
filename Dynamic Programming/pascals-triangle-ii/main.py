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

    @staticmethod
    def get_row_2(row_index) -> list[int]:
        row_elements = (row_index + 1) * [1]

        count = row_index

        for i in range(1, row_index):
            row_elements[i] = int(row_elements[i - 1] * count / i)
            count -= 1

        return row_elements


if __name__ == '__main__':
    print(Solution.get_row(3))
