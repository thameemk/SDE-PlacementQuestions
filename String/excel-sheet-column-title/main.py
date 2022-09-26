#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Mon, 26 Sep 2022 at 11:01 pm India Standard Time
#  Last modified time : Mon, 26 Sep 2022 at 11:01 pm India Standard Time

"""
Link: https://leetcode.com/problems/excel-sheet-column-title/
Tags: Math, String
"""


def convert_to_title(column_number: int) -> str:
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if column_number <= 26:
        return alphabets[column_number - 1]

    return convert_to_title((column_number-1) // 26) + convert_to_title(column_number % 26)


if __name__ == '__main__':
    print(convert_to_title(701))
