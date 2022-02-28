#  Project : SDE Placement Questions
#  Filename : LongestCommonPrefix.py
#  Author : thameem
#  Created  time : Sun, 27 Feb 2022 at 11:54 PM India Standard Time
#  Last modified time : Sun, 27 Feb 2022 at 11:54 PM India Standard Time
from typing import Optional


class LongestCommonPrefix:

    @staticmethod
    def find_longest_common_prefix(strings: list[str]) -> Optional[str]:
        prefix = min(strings, key=len)
        strings.remove(prefix)
        for each in strings:
            while not each.startswith(prefix) and prefix != '':
                prefix = prefix[:-1]

        return prefix


if __name__ == '__main__':
    response = LongestCommonPrefix.find_longest_common_prefix(strings=["dog", "racecar", "car"])
    # response = LongestCommonPrefix.find_longest_common_prefix(strings=["flower", "flow", "flight"])
    print(response)
