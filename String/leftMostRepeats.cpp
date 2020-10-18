#include<iostream>
#include<climits>
#include<stdio.h>
using namespace std;
int findRepeat(string &s)
{    
    int res=INT_MAX;
    int temp[256];
    for(int k=0;k<255;k++)
        temp[k]=-1;
    for(int i=0;i<s.length();i++)
    {
        if(temp[s[i]]==-1)
            temp[s[i]]=i;
        else
            res = min(res,temp[s[i]]);                   
    }
    return (res==INT_MAX)?-1:res;
}
int main()
{
    string s;  
    cin>>s;
    cout<<findRepeat(s)<<endl;
    return 0;
}