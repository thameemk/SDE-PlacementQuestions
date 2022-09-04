"""
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self._get_depth(root.left, root.right)+1

    def _get_depth(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> int:

        if left is None and right is None:
            return 0

        elif left is None:
            return self._get_depth(right.left, right.right)+1

        elif right is None:
            return self._get_depth(left.left, left.right)+1

        else:
            _right_depth = self._get_depth(right.left, right.right)
            _left_depth = self._get_depth(left.left, left.right)

            if _right_depth > _left_depth:
                return _left_depth+1
            else:
                return _right_depth+1
