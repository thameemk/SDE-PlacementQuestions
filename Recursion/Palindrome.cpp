#include<iostream>
using namespace std;
bool palindrome(string s,int l,int n=0)
{
    if(n==l || n>l)
        return true;
    if(s[n]!=s[l])
        return false;
    return palindrome(s,l-1,n+1);    
}
int main()
{
    string s;
    cout<<"\nEnter a string: ";        
    cin>>s;
    cout<<palindrome(s,s.length()-1);
    return 0;
}