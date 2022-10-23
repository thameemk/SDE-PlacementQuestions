#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class NumArray
{
    vector<int> nums;
public:
    NumArray(vector<int> &nums)
    {
        this->nums = nums;
    }

    int sumRange(int left, int right)
    {
        // int _sum = 0;

        // for (int i=left;i<=right;i++)
        // {
        //     _sum =_sum + this->nums[i];
        // }

        // return _sum;
        return accumulate(this->nums.begin()+left,this->nums.begin()+right+1,0);
    }
};

int main()
{
    vector<int> nums = {-2, 0, 3, -5, 2, -1};
    NumArray obj = NumArray(nums);
    cout << obj.sumRange(0, 2) << " ";
    return 0;
}