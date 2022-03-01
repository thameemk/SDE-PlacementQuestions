#  Project : SDE Placement Questions
#  Filename : GroupAnagrams.py
#  Author : thameem
#  Created  time : Mon, 28 Feb 2022 at 11:03 PM India Standard Time
#  Last modified time : Mon, 28 Feb 2022 at 11:03 PM India Standard Time


class GroupAnagrams:
    @staticmethod
    def group_the_anagrams(strings: list[str]) -> list[list[str]]:
        result = []
        hash_map = {}
        for string in strings:
            string_original = string
            string = list(string)
            string.sort()
            string = "".join(string)
            if string not in hash_map.keys():
                hash_map[string] = [string_original]
            else:
                hash_map[string].append(string_original)

        for key in hash_map.keys():
            result.append(hash_map[key])

        return result


if __name__ == '__main__':
    response = GroupAnagrams.group_the_anagrams(strings=["eat", "tea", "tan", "ate", "nat", "bat"])
    # response = GroupAnagrams.group_the_anagrams(strings=["", ""])
    print(response)
