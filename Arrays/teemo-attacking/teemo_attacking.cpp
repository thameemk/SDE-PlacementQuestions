#include<iostream>

using namespace std;

int find_poisoned_duration(vector<int>& time_series, int duration)
{
    int total_seconds = 0;
    int temp = 0;

    for(auto& it : time_series)
    {
        total_seconds += it + duration - max(temp,it);
        temp = it + duration;
    }

    return total_seconds;
}

int main()
{
    vector<int> time_series = {1,4};
    int duration = 4;
    cout<<"\n"<<find_poisoned_duration(time_series,duration<<"\n";
    return 0;
}