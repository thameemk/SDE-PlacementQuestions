#  Project : SDE Placement Questions
#  Filename : island_perimeter.py
#  Author : thameem
#  Current modification time : Mon, 12 Dec 2022 at 11:53 pm India Standard Time
#  Last modified time : Mon, 12 Dec 2022 at 11:53 pm India Standard Time
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    number_of_islands = 0
    adjacent_islands = 0

    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == 1:
                number_of_islands += 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    adjacent_islands += 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    adjacent_islands += 1

    return (number_of_islands * 4) - (adjacent_islands * 2)


if __name__ == '__main__':
    _grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(island_perimeter(_grid))
