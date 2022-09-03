"""
Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        node_at_middle = len(nums)//2

        return TreeNode(
            val=nums[node_at_middle],
            left=self.sorted_array_to_bst(nums[:node_at_middle]),
            right=self.sorted_array_to_bst(nums[node_at_middle+1:])
        )
