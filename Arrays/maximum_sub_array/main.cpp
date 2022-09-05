#include <iostream>
#include <vector>
using namespace std;

int maximum_sub_array(vector<int>& nums)
{
   int temporary_sum = nums[0];
   int actual_sum = nums[0];
   for (int i=1;i<nums.size();i++)
   {
        if (temporary_sum>=0)
            temporary_sum = temporary_sum + nums[i];
        else
            temporary_sum = nums[i];

        if (temporary_sum>actual_sum)
            actual_sum = temporary_sum;
   }

   return actual_sum;
}

int main()
{
    vector<int> nums =  {1};
    int response = maximum_sub_array(nums);
    cout<<"\n"<<response<<"\n";
    return 0;
}