"""
Link: https://leetcode.com/problems/add-binary/
"""


def add_binary(a: str, b: str) -> str:
    sum = bin(int(a,2)+int(b,2))
    return sum[2:]


if __name__ == '__main__':

    response = add_binary(a='11', b='1')
    print(response)
