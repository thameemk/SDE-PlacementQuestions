#include <iostream>
#include <vector>

using namespace std;

int find_max_consecutive_ones(vector<int>& nums)
{
    int max_consecutives = 0;
    int temp = 0;

    for(int i=0;i<nums.size();i++)
    {
        if(nums[i]==1)
        {
            temp++;
        }
        else
        {
            max_consecutives = max(temp,max_consecutives);
            temp = 0;
        }
    }

    return max(temp,max_consecutives);
}

int main()
{
    vector<int> nums = {1, 0, 1, 1, 0, 1};

    return 0;
}