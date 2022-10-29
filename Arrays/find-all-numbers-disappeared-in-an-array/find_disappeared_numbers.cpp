#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> find_disappeared_numbers(vector<int> &nums)
{
    unordered_set<int> set_nums(begin(nums), end(nums));
    vector<int> res;

    for (int i = 1; i <= nums.size(); i++)
    {
        if (!set_nums.count(i))
            res.push_back(i);
    }

    return res;
}

int main()
{

    vector<int> nums = {4, 3, 2, 7, 7, 2, 3, 1};
    vector<int> result = find_disappeared_numbers(nums);
    for (auto n : result)
        cout << n << " ";
    return 0;
}