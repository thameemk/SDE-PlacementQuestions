#include<iostream>
using namespace std;
bool isAnargom(string &s1, string &s2)
{    
    if(s1.length()!=s2.length())
        return false;
    char count[256] = {0};    
    for(int i=0;i<s1.length();i++)
        count[s1[i]]++;
    for(int j=0;j<s2.length();j++)
        count[s2[j]]--;
    for(int k=0;k<256;k++)
        if(count[k]!=0)
            return false;                
    return true;
}
int main()
{
    string s1,s2;  
    cin>>s1>>s2;
    cout<<isAnargom(s1,s2)<<endl;
    return 0;
}