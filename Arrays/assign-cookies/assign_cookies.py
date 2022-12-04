#  Project : SDE Placement Questions
#  Filename : assign_cookies.py
#  Author : thameem
#  Current modification time : Sun, 4 Dec 2022 at 12:00 am India Standard Time
#  Last modified time : Sun, 4 Dec 2022 at 12:00 am India Standard Time


def find_content_children(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    child, cookie = 0, 0

    while child != len(g) and cookie != len(s):
        if s[cookie] >= g[child]:
            cookie += 1
            child += 1
        else:
            cookie += 1

    return child


if __name__ == '__main__':
    res = find_content_children(g=[1, 2, 3], s=[1, 1])
    print(res)
