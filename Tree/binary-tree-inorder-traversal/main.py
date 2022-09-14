"""
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        response = []

        if root.left is not None:
            response.extend(self.inorder_traversal(root.left))

        response.append(root.val)   
            
        if root.right is not None:
            response.extend(self.inorder_traversal(root.right))

        return response
