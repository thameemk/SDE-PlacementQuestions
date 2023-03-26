#include <iostream>

using namespace std;

string check_palindrome(int l, int r, string res, string s)
{
    while (l >= 0 and r < s.length() and s[l] == s[r])
    {
        if ((r - l - 1) > res.length())
        {
            res = s.substr(l, r + 1);
        }

        l--;
        r++;
    }

    return res;
}

string longestPalindrome(string s)
{
    string res = "";
    int res_len = 0;

    for (int i = 0; i < s.length(); i++)
    {

        res = check_palindrome(i, i, res, s);
        res = check_palindrome(i, i + 1, res, s);
    }

    return res;
}

int main()
{
    cout<<longestPalindrome("b")<<"\n";
    return 0;
}