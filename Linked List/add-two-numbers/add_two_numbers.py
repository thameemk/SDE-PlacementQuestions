

"""
Link: https://leetcode.com/problems/add-two-numbers/submissions/
Tags: Linked List, Math, Recusrion
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

  

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    first_num = ""
    second_num = ""
    
    if l1:
        num = l1
        while num:
            first_num = str(num.val)+first_num
            num = num.next
            
    if l2:
        num = l2
        while num:
            second_num = str(num.val)+second_num
            num = num.next
            
    sum_of_num = int(first_num)+int(second_num)
            
    digits = list(str(sum_of_num))
    
    res = ListNode()
    
    temp = res
    
    while digits:
        digit = digits.pop()
        temp.next = ListNode(digit)
        temp = temp.next
        
    return res.next
            