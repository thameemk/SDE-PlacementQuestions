"""
Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def max_depth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        return self._get_depth(root.left, root.right)

    def _get_depth(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> int:

        self.depth = 0

        if left is None and right is None:
            self.depth += 0

        elif left is None:
            self.depth += self._get_depth(right.left, right.right)

        elif right is None:
            self.depth += self._get_depth(left.left, left.right)

        else:
            _right_depth = self._get_depth(right.left, right.right)
            _left_depth = self._get_depth(left.left, left.right)

            if _right_depth > _left_depth:
                self.depth += _right_depth
            else:
                self.depth += _left_depth

        return self.depth
