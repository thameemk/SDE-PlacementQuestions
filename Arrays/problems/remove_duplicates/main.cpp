/*
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
*/

#include <iostream>
#include <vector>
using namespace std;

int remove_duplicates(vector<int> &numbers)
{
    int i = 0;
    for (int j = 1; j < numbers.size(); j++)
    {
        if (numbers[j] != numbers[i])
        {
            numbers[++i] = numbers[j];
        }
    }
    return i + 1;
}

int main()
{
    vector<int> numbers = {1, 1, 2};
    cout << remove_duplicates(numbers);
    return 0;
}