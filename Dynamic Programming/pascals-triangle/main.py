"""
Link: https://leetcode.com/problems/pascals-triangle/
"""

from typing import List


class Solution:

    def generate_pascals_triangle(self, num_rows: int) -> List[List[int]]:
        pascals_triangle = [[1]]

        if num_rows == 1:
            return pascals_triangle

        for i in range(1, num_rows):

            pascals_triangle.append([1])

            for j in range(1, i):
                pascals_triangle[i].append(pascals_triangle[i -
                                                            1][j] + pascals_triangle[i - 1][j - 1])

            pascals_triangle[i].append(1)

        return pascals_triangle


if __name__ == '__main__':
    print(Solution().generate_pascals_triangle(num_rows=5))
