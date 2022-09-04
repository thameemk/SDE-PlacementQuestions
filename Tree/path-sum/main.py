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
    def has_path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pass