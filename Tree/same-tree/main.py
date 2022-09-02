"""
Link: https://leetcode.com/problems/same-tree/
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.is_same_tree(p.right, q.right) and self.is_same_tree(p.left, q.left)

        return False


if __name__ == '__main__':

    node = TreeNode()
    node.val = 1

    root_1 = TreeNode()
    root_1.val = 1
    root_1.left = node

    root_2 = TreeNode()
    root_2.val = 1
    root_2.right = node

    solution = Solution().is_same_tree(root_1, root_2)
    print(solution)
