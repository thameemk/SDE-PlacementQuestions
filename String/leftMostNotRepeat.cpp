#include<iostream>
#include<climits>
using namespace std;
int findNotRepeat(string &s)
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
            temp[s[i]]=-2;                  
    }
    for(int j=0;j<256;j++)
    {
        if(temp[j]>=0)
            res = min(res,temp[j]);
    }
    return (res==INT_MAX)?-1:res;
}
int main()
{
    string s;  
    cin>>s;
    cout<<findNotRepeat(s)<<endl;
    return 0;
}