#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

void push_to_node(Node **head_reference, int data)
{
    Node *new_node = new Node();
    new_node->data = data;
    new_node->next = (*head_reference);
    (*head_reference) = new_node;
}

void print_linked_list(Node *node)
{
    while (node!=NULL)
    {
        cout<<node->data<<"\n";
        node = node->next;
    }
    
}

int main()
{
    Node *head = new Node();
    head->data = 1;
    head->next = NULL;
    push_to_node(&head, 2);
    print_linked_list(head);
    return 0;
}