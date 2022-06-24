#include <iostream>

using namespace std;

int str_str(string haystack, string needle)
{
    return haystack.find(needle);
}

int main()
{
    string haystack = "hello";
    string needle = "oo";

    int response = str_str(haystack, needle);

    cout << "\n"
         << response << "\n";

    return 0;
}