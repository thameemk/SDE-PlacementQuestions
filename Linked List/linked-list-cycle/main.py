"""
Link: https://leetcode.com/problems/linked-list-cycle/
Topics: Linked List, Hash Table, Two Pointers
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        
        visited_node_values = set()
        
        while head:
            if head in visited_node_values:
                return True
            else:
                visited_node_values.add(head)
                head = head.next
            
        return False


        