#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int missing_number(vector<int> &nums)
{
    int len_of_nums = nums.size();

    int actual_sum = (len_of_nums * (len_of_nums + 1)) / 2;

    int given_sum = accumulate(nums.begin(), nums.end(), 0);

    return actual_sum - given_sum;
}

int main()
{
    vector<int> nums = {9, 6, 4, 2, 3, 5, 7, 0, 1};
    cout << missing_number(nums);
    return 0;
}