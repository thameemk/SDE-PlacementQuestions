# ***Linked List***

- Linear Data Structure
- Elements are not stored in continues memmory locations
- Each elements are linked using pointers
  
  **Advatages**

- Dynamic size
- Ease of insertion and deletion 
  
  **Drawbacks**
- Caching doesn't work
- Random access not possible
- Additional memmory allocation for pointers

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
  - Simple linked list with 4 nodes