"""
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Tags: Stack, Tree, Depth-First-Search, Binary Tree
"""

from typing import List, Optional
from urllib import response


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        response = []

        if root.left:
            response.extend(self.postorder_traversal(root.left))
        
        if root.right:
            response.extend(self.postorder_traversal(root.right))

        response.append(root.val)

        return response