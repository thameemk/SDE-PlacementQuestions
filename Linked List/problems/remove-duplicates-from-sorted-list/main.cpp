#include<iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* delete_duplicates(ListNode* head) {
        if(head==NULL){
            return head;
        }

        ListNode* temp = head;

        while (head->next!=NULL)
        {
            if(head->val==head->next->val){
                head->next = head->next->next;
            }
            else{
                head = head->next;
            }
        }

        return temp;
        
    }
};

int main()
{

    ListNode* first_node=NULL;
    ListNode* second_node=NULL;
    ListNode* third_node=NULL;

    first_node = new ListNode();
    second_node = new ListNode();
    third_node = new ListNode();
    
    first_node->val = 1;
    second_node->val = 1;
    third_node->val = 2;

    first_node->next = second_node;
    second_node->next = third_node;

    Solution list_node = Solution();

    list_node.delete_duplicates(first_node);

    return 0;
}