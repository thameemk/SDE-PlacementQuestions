#  Project : SDE Placement Questions
#  Filename : longest_palindromic_substring.py
#  Author : thameem
#  Current modification time : Sat, 25 Mar 2023 at 2:41 pm India Standard Time
#  Last modified time : Sat, 25 Mar 2023 at 2:41 pm India Standard Time


def check_palindrome(l, r, len_of_string, s, res_length, res):
    while l >= 0 and r < len_of_string and s[l] == s[r]:
        if (r - l + 1) > res_length:
            res_length = r - l + 1
            res = s[l:r + 1]

        l -= 1
        r += 1

    return res, res_length


def longest_palindrome(s: str) -> str:
    res = ""

    res_length = 0

    len_of_string = len(s)

    for i in range(len_of_string):
        res, res_length = check_palindrome(i, i, len_of_string, s, res_length, res)
        res, res_length = check_palindrome(i, i + 1, len_of_string, s, res_length, res)

    return res


if __name__ == '__main__':
    print(longest_palindrome(s="babad"))
