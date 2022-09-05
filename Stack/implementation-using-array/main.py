
from array import array


class Stack:
    def __init__(self) -> None:
        self.stack = array('i', [])

    def push_to_stack(self, item: int) -> bool:
        self.stack.append(item)
        return True

    def pop_from_stack(self) -> bool:
        if len(self.stack) == 0:
            return False
        else:
            self.stack.pop()

    def show_stack_elements(self) -> None:
        for element in self.stack:
            print(element)


if __name__ == '__main__':
    stack = Stack()
    stack.push_to_stack(1)
    stack.push_to_stack(2)
    stack.push_to_stack(3)
    stack.pop_from_stack()
    stack.show_stack_elements()
