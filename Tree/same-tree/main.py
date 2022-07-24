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
    #todo - not yet passed all test cases
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if  self.inorder_traversal(p) ==  self.inorder_traversal(q):
            return True
        else:
            return False

    def inorder_traversal(self, root: Optional[TreeNode]) -> Optional[List[int]]:
        if root is None:
            return []

        response = []

        if root.left is None and root.right is None:
             response.append(root.val)
        else:
            if root.left is not None:
                response.extend(self.inorder_traversal(root.left))
            else:
                response.append(0)

            response.append(root.val)

            if root.right is not None:
                response.extend(self.inorder_traversal(root.right))
            else:
                response.append(0)

        return response


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
