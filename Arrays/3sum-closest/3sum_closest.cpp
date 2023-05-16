#include<vector>

using namespace std;

int three_sum_closest(vector<int>& nums, int target) {

        sort(nums.begin(),nums.end());
        int closest_sum = nums[0]+nums[1]+nums[2];
        int len_of_nums = nums.size();

        for(int i=0;i<len_of_nums;i++)
        {
            int left = i+1;
            int right = len_of_nums-1;

            while(left<right){

                int sum_of_current_elements = nums[i]+nums[left]+nums[right];

                if(sum_of_current_elements==target)
                    return sum_of_current_elements;
                else if (sum_of_current_elements<target)
                    left++;
                else
                    right--;

                if(abs(sum_of_current_elements-target)<abs(closest_sum-target))
                    closest_sum = sum_of_current_elements;
            }
        }


        return closest_sum;

    }