# Longest Substring Without Repeating Characters

# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(s: str) -> int:
    max_length = 0
    unique_characters = set()

    i = j = 0

    while (i < len(s)):

        if s[i] in unique_characters:
            unique_characters.remove(s[j])
            j += 1
        else:
            unique_characters.add(s[i])
            i += 1
            max_length = max(max_length, i-j)

    return max_length
