
#include <vector>
#include <iostream>

using namespace std;

int maxArea(vector<int> &height)
{
    int no_of_lines = height.size();
    int max_area = 0;
    int left = 0;
    int right = no_of_lines - 1;
    while (left < right)
    {
        int current_area = min(height[left], height[right]) * (right - left);
        max_area = max(current_area, max_area);

        if (height[left] < height[right])
        {
            left++;
        }
        else
        {
            right--;
        }
    }

    return max_area;
}

int main()
{
    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    
    cout<<maxArea(height)<<"\n";

    return 0;
}