
#include <iostream>
#include <vector>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution
{
public:
    vector<int> inorderTraversal(TreeNode *root)
    {
        if (root == NULL)
        {
            return {};
        }

        vector<int> response = {};

        if (root->left != NULL)
        {
            vector<int> child = Solution().inorderTraversal(root->left);
            response.insert(response.end(), child.begin(), child.end());
        }

        response.push_back(root->val);

        if (root->right != NULL)
        {
            vector<int> child = Solution().inorderTraversal(root->right);
            response.insert(response.end(), child.begin(), child.end());
        }

        return response;
    }
};