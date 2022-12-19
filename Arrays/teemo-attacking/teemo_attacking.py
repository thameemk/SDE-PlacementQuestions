#  Project : SDE Placement Questions
#  Filename : teemo_attacking.py
#  Author : thameem
#  Current modification time : Wed, 14 Dec 2022 at 10:49 pm India Standard Time
#  Last modified time : Wed, 14 Dec 2022 at 10:49 pm India Standard Time
from typing import List


def find_poisoned_duration(time_series: List[int], duration: int) -> int:
    total_seconds = 0
    temp = 0

    for each in time_series:
        total_seconds += each + duration - max(temp, each)
        temp = each + duration

    return total_seconds


if __name__ == '__main__':
    print(find_poisoned_duration([1, 4], 2))
    print(find_poisoned_duration([1, 2], 2))
    print(find_poisoned_duration([1, 2, 3, 4, 5, 6, 7, 8, 9], 100000))

"""
1-> 1 to 3 -> 2s
4-> 4 to 6 -> 2s
total      -> 4s


1-> 1 to 3 -> 2s
2-> 2 to 4 -> 2s
at 3 reset -> total -> 3s
"""
