#include <iostream>
#include <string>

//   Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        string first_num = "";
        string second_num = "";
        if (l1)
        {
            ListNode *num = l1;
            while (num)
            {
                first_num = first_num + to_string(num->val);
                num = num->next;
            }
        }

        if (l2)
        {
            ListNode *num = l2;
            while (num)
            {
                second_num = second_num + to_string(num->val);
                num = num->next;
            }
        }

        int sum = stoi(first_num) + stoi(second_num);

        ListNode *res = new ListNode();

        ListNode *temp = res;

        if (sum != 0)
        {
            while (sum)
            {
                int digit = sum % 10;
                sum = sum / 10;

                temp->next = new ListNode(digit);
                temp = temp->next;
            }
            return res->next;
        }

        else
        {
            res->val = 0;
            return res;
        }
    }
};