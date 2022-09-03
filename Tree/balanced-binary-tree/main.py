"""
Link: https://leetcode.com/problems/balanced-binary-tree/
"""


from math import fabs
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        self.balanced = True

        self._get_height(root)

        return self.balanced

    def _get_height(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        _left_depth = self._get_height(root.left)
        _right_depth = self._get_height(root.right)

        if abs(_left_depth-_right_depth) > 1:
            self.balanced = False

        return max(_left_depth+1, _right_depth+1)
