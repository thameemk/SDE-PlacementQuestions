#include<vector>
#include<set>

using namespace std;

vector<vector<int>> threeSum(vector<int> &nums)
{

    int len_of_array = nums.size();

    sort(nums.begin(), nums.end());

    set<vector<int>> result;

    for (int i = 0; i < len_of_array; i++)
    {
        int left = i + 1;
        int right = len_of_array - 1;

        while (left < right)
        {

            int sum = nums[i] + nums[left] + nums[right];

            if (sum == 0)
            {
                result.insert({nums[i], nums[left], nums[right]});
                left++;
                right--;
            }

            else if (sum < 0)
                left++;
            else
                right--;
        }
    }

    vector<vector<int>> output;

    copy(result.begin(), result.end(), back_inserter(output));

    return output;
}