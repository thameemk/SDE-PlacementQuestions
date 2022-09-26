#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Sun, 25 Sep 2022 at 7:12 pm India Standard Time
#  Last modified time : Sun, 25 Sep 2022 at 7:12 pm India Standard Time

"""
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Tags: Hash Table, Linked List, Two Pointers
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        hash_map = {}

        t_head_a = head_a
        t_head_b = head_b

        while t_head_a is not None:
            hash_map[id(t_head_a)] = t_head_a
            t_head_a = t_head_a.next

        while t_head_b is not None:
            if id(t_head_b) in hash_map:
                return t_head_b
            t_head_b = t_head_b.next

        return None
