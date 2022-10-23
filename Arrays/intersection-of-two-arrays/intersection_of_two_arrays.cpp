#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
{
    vector<int> _intersection;
    set<int> n1,n2;

    for (auto n:nums1)
        n1.insert(n);
    
    for (auto n:nums2)
        n2.insert(n);

    for (auto n:n1){
        if (n2.find(n)!=n2.end())
            _intersection.push_back(n);
    }

    return _intersection;
    // todo: optimize with n+m
}

int main()
{
    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};
    intersection(nums1,nums2);
    return 0;
}