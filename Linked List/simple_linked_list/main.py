class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_elements(self):
        temp_element = self.head
        while(temp_element):
            print(temp_element.data)
            temp_element = temp_element.next



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second_node = Node(2)
    linked_list.head.next = second_node
    second_node.next = Node(3)

    linked_list.print_elements()
