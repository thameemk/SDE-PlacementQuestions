"""
Problem Link : https://leetcode.com/problems/implement-strstr/
"""


def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == '__main__':

    haystack = "hello"
    needle = "oo"

    response = str_str(haystack, needle)

    print(response)
