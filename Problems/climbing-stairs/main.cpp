#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int climbStairs(int n)
    {
        if (n == 1)
        {
            return 1;
        }
        else
        {
            vector<int> fibonacci_series = {1, 1};
            for (int i = 2; i < n + 1; i++)
            {
                int next_number = fibonacci_series[i-1]+fibonacci_series[i-2];
                fibonacci_series.push_back(next_number);
            }

            return fibonacci_series[n];
        }
    }
};

int main()
{
    Solution solution = Solution();
    int number_ways = solution.climbStairs(4);
    cout<<"\n"<<number_ways<<"\n";
    return 0;
}