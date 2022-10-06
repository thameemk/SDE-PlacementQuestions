#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Wed, 5 Oct 2022 at 10:27 pm India Standard Time
#  Last modified time : Wed, 5 Oct 2022 at 10:27 pm India Standard Time


"""
Link: https://leetcode.com/problems/isomorphic-strings/
Tags: Hash Table, String
"""


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_map = {}
    # todo - consider all test cases
    for index, each in enumerate(s):
        t_chara = t[index]
        if t_chara not in hash_map:
            hash_map[t_chara] = index
            first_part = t[:index]
            second_part = t[index:]
            second_part = second_part.replace(t_chara, each)
            t = first_part + second_part
            a = 1

    if t == s:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_isomorphic("egg", "add"))
    print(is_isomorphic("foo", "bar"))
    print(is_isomorphic("paper", "title"))
    print(is_isomorphic("badc", "baba"))
