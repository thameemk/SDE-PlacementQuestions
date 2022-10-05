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

    for index, each in enumerate(s):
        if each not in hash_map:
            hash_map[each] = index
            t_chara = t[index]
            t = t.replace(t_chara, each)

    if t == s:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_isomorphic("egg", "add"))
