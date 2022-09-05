from typing import Optional


class ListNode:
    def __init__(self, next: Optional['ListNode'], val: int = 0) -> None:
        self.val = val
        self.next = next


def merge_two_linked_list(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return list1

    if list1 and not list2:
        return list1

    if list2 and not list1:
        return list2

    first, second = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = first

    
    while first and second:
        while first.next and first.next.val < second.val:
            first = first.next

        first.next, second = second, first.next
        first = first.next

    return head


if __name__ == '__main__':
    pass
