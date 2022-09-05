"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        temp = head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return temp


if __name__ == '__main__':
    fifth_node = ListNode(val=3)

    fourth_node = ListNode(val=3, next=fifth_node)

    third_node = ListNode(val=2, next=fourth_node)

    second_node = ListNode(val=1, next=third_node)

    first_node = ListNode(val=1, next=second_node)

    Solution().delete_duplicates(head=first_node)
