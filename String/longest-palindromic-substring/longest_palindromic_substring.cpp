#include <iostream>

using namespace std;

void check_palindrome(int l,int r,string &res,string s, int &res_len, int &s_len)
    {
        while(l>=0 && r<s_len && s[l]==s[r])
        {
            if((r-l+1)>res_len)
            {
                res_len = r-l+1;
                res = s.substr(l,res_len);
            }

            l--;
            r++;
        }

    }

string longestPalindrome(string s)
{
    string res = "";
    int res_len = 0;
    int s_len = s.length();

    for(int i=0;i<s_len;i++)
    {

        check_palindrome(i,i,res,s,res_len,s_len);
        check_palindrome(i,i+1,res,s,res_len,s_len);

    }

    return res;
}

int main()
{
    cout<<longestPalindrome("b")<<"\n";
    return 0;
}