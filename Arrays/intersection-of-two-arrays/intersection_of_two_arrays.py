#  Project : SDE Placement Questions
#  Filename : intersection_of_two_arrays.py
#  Author : thameem
#  Current modification time : Sun, 23 Oct 2022 at 11:06 pm India Standard Time
#  Last modified time : Sun, 23 Oct 2022 at 11:06 pm India Standard Time


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))

    _intersection = set()

    if len(nums1) > (len(nums2)):
        for num in nums2:
            if num in nums1:
                _intersection.add(num)
    else:
        for num in nums1:
            if num in nums2:
                _intersection.add(num)

    return list(_intersection)


if __name__ == '__main__':
    print(intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
