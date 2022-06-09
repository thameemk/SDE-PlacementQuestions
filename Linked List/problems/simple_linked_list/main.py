class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second_node = Node(2)
    linked_list.head.next = second_node
    second_node.next = Node(3)
