#include <iostream>

using namespace std;

#define MAX_STACK_SIZE 50

class Stack
{
  int top_of_stack;
  int stack_array[MAX_STACK_SIZE];

public:
  Stack();
  bool push_to_stack(int);
  bool pop_from_stack();
  void show_stack();
};

Stack::Stack()
{
  top_of_stack = -1;
}

bool Stack::push_to_stack(int element)
{
  if (top_of_stack >= (MAX_STACK_SIZE - 1))
  {
    cout << "\nSTACK OVER FLOW\n";
    return false;
  }
  else
  {
    stack_array[++top_of_stack] = element;
    cout << "\nPUSHED TO STACK\n";
    return true;
  }
}

bool Stack::pop_from_stack()
{
  if (top_of_stack < 0)
  {
    cout << "\nSTACK UNDER FLOW\n";
    return false;
  }
  else
  {
    stack_array[--top_of_stack];
    return true;
  }
}

void Stack::show_stack()
{
  if (top_of_stack < 0)
  {
    cout << "\nSTACK IS EMPTY\n";
  }
  else
  {
    cout << "\nTHE ELEMENTS ARE : ";
    for (int i = 0; i <= top_of_stack; i++)
    {
      cout << stack_array[i] << " ";
    }
  }
}

int main()
{
  class Stack s;
  s.push_to_stack(1);
  s.push_to_stack(2);
  s.push_to_stack(3);
  s.pop_from_stack();
  s.show_stack();
  return 0;
}