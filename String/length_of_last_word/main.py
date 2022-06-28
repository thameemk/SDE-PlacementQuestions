"""

Link: https://leetcode.com/problems/length-of-last-word/

"""


def length_of_last_word(s: str) -> int:
    word_list = s.split(" ")
    word_list[:] = sorted(set(word_list),key=word_list.index)
    if word_list[-1]=="":
        return len(word_list[-2])
    else:
        return len(word_list[-1])


if __name__ == '__main__':
    response = length_of_last_word(s="a ")
    print(response)
