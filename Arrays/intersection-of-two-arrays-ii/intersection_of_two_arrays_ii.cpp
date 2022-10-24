#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
{
    vector<int> _intersection;

    for (auto n : nums2)
    {
        vector<int>::iterator it = find(nums1.begin(), nums1.end(), n);
        if (it != nums1.end())
        {
            _intersection.push_back(n);
            nums1.erase(it);
        }
    }

    return _intersection;
}

int main()
{
    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};
    vector<int> result = intersect(nums1, nums2);
    for (auto n : result)
        cout << n << " ";
    return 0;
}