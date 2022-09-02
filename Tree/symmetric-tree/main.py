"""
Problem Link: https://leetcode.com/problems/symmetric-tree/
"""

from logging import root
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_symmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        return self._symmetric(root.left, root.right)

    def _symmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return self._symmetric(left.left, right.right) and self._symmetric(right.left, left.right)
