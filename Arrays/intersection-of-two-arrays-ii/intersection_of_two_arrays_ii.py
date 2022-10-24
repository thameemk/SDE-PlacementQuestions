#  Project : SDE Placement Questions
#  Filename : intersection_of_two_arrays.py
#  Author : thameem
#  Current modification time : Sun, 23 Oct 2022 at 11:06 pm India Standard Time
#  Last modified time : Sun, 23 Oct 2022 at 11:06 pm India Standard Time


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    _intersect = []

    for num in nums2:
        if num in nums1:
            _intersect.append(num)
            nums1.remove(num)

    return _intersect


if __name__ == '__main__':
    print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
