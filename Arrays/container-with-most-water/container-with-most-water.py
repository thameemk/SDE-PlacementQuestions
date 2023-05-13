#  Project : SDE Placement Questions
#  Filename : container-with-most-water.py
#  Author : thameem
#  Current modification time : Sat, 13 May 2023 at 11:56 pm India Standard Time
#  Last modified time : Sat, 13 May 2023 at 11:56 pm India Standard Time

# Link: https://leetcode.com/problems/container-with-most-water/submissions/


def get_max_area(height: list[int]) -> int:
    no_of_lines = len(height)
    left, right = 0, no_of_lines - 1
    max_area = 0
    while left < right:

        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
