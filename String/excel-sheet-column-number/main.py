#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Mon, 26 Sep 2022 at 11:21 pm India Standard Time
#  Last modified time : Mon, 26 Sep 2022 at 11:21 pm India Standard Time
"""
Link: https://leetcode.com/problems/excel-sheet-column-number/
Tags: String, Math
"""


def title_to_number(column_title: str) -> int:
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    column_title_alphabets = list(column_title)[::-1]

    column_number = 0

    for index, alphabet in enumerate(column_title_alphabets):
        alphabet_num = alphabets.index(alphabet) + 1
        column_number += alphabet_num * pow(26, index)

    return column_number


if __name__ == '__main__':
    print(title_to_number('A'))
