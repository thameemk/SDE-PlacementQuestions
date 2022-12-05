#include <iostream>
#include <vector>

using namespace std;

int find_content_children(vector<int> &g, vector<int> &s)
{

    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int child = 0;
    int cookie = 0;

    while (child != g.size() && cookie != s.size())
    {
        if (s[cookie] >= g[child])
        {
            cookie++;
            child++;
        }
        else
        {
            cookie++;
        }
    }

    return child;
}

int main()
{
    vector<int> g = {1, 2, 3};
    vector<int> s = {1, 1};
    cout << "\n"
         << find_content_children(g,s) << "\n";
    return 0;
}