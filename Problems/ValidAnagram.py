#  Project : SDE Placement Questions
#  Filename : ValidAnagram.py
#  Author : thameem
#  Created  time : Mon, 28 Feb 2022 at 10:32 PM India Standard Time
#  Last modified time : Mon, 28 Feb 2022 at 10:32 PM India Standard Time

class ValidAnagram:
    @staticmethod
    def is_anagram(s_1: str, s_2: str) -> bool:
        if not len(s_1) == len(s_2):
            return False
        else:
            return all(s_1.count(i) == s_2.count(i) for i in s_2)


if __name__ == '__main__':
    response = ValidAnagram.is_anagram(s_1="car", s_2="rat")
    print(response)
