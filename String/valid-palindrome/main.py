"""
Link: https://leetcode.com/problems/valid-palindrome/
"""

import re


class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = ''.join([character.lower() for character in s if character.isalnum()])
        return s == s[::-1]


if __name__ == '__main__':
    print(Solution().is_palindrome(s="rAce a car"))
    print(Solution().is_palindrome(s=" "))