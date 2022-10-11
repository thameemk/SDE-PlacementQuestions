#include <iostream>
#include <vector>
#include <map>
using namespace std;

bool contains_nearby_duplicate(vector<int> &nums, int k)
{
    map<int, int> duplicate_values;

    for (int i = 0; i < nums.size(); i++)
    {
        if (duplicate_values.count(nums[i]) != 0 and abs(i - duplicate_values[nums[i]]) <= k)
        {
            return true;
        }
        else
        {
            duplicate_values[nums[i]] = i;
        }
    }

    return false;
}

int main()
{
    vector<int> nums = {1, 2, 3, 1};
    int k = 3;
    cout << contains_nearby_duplicate(nums, k);
    return 0;
}