#include <string>
#include <set>

using namespace std;


int length_of_longest_substring(string s)
{

    int max_length, i, j = 0;

    set<char> unique_char;

    while (i < s.length())
    {
        if (unique_char.find(s[i]) != unique_char.end())
        {
            unique_char.erase(s[j]);
            j++;
        }
        else
        {
            unique_char.insert(s[i]);
            i++;
            max_length = max(max_length, i - j);
        }
    }

    return max_length;
}