"""
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Topics: Stack, Tree, Depth-First Search, Binary Tree
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        response = []

        response.append(root.val)

        if root.left:
            response.extend(self.preorder_traversal(root.left))

        if root.right:
            response.extend(self.preorder_traversal(root.right))

        return response