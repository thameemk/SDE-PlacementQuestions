
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push_to_linked_list(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        temp_node = self.head
        while(temp_node):
            print(temp_node.data)
            temp_node = temp_node.next




if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    linked_list.push_to_linked_list(2)
    linked_list.print_linked_list()

