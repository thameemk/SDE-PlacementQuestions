# ***Linked List***

- Linear Data Structure
- Elements are not stored in continues memory locations
- Each element is linked using pointers / reference field 
  
  **Advantages**

- Dynamic size
- Ease of insertion and deletion 
  
  **Drawbacks**
- Caching doesn't work
- Random access not possible
- Additional memory allocation for pointers / reference field

  **C++**
  ```cpp
  class Node{
    public:
      int data;
      Node *next;
  };

  ```
  **Python**
  ```py
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

  class LinkedList:
    def __init__(self):
      self.head = None
  ```

  **Example**
  - Simple linked list with 4 nodes - [C++](simple_linked_list/main.cpp) - [Python](simple_linked_list/main.py)
  - Inserting nodes - [C++](inserting_nodes/main.cpp) - [Python](inserting_nodes/main.py)
  - Merge Two Sorted Linked Lists - [Python](merge-two-sorted-linked-lists/main.py)
  - [Remove Duplicates from Sorted List](https://leetcode.com/remove-duplicates-from-sorted-list/) - [Python](remove-duplicates-from-sorted-list/main.py)