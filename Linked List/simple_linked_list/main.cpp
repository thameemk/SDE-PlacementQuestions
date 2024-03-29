#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

void print_linked_list(Node* node)
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
    Node *second_node = new Node();
    Node *third_node = new Node();

    head->data = 1;
    head->next = second_node;
    second_node->data = 2;
    second_node->next = third_node;
    third_node->data = 3;
    third_node->next = NULL;

    print_linked_list(head);
    
    return 0;
}