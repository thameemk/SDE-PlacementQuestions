"""
Link: https://leetcode.com/problems/path-sum/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:

        if root is None:
            return False

        if root.left is None and root.right is None and root.val == target_sum:
            return True

        target_sum -= root.val

        return (self.has_path_sum(root.left, target_sum) or self.has_path_sum(root.right, target_sum))
