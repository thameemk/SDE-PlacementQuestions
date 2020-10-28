#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;


int getNum(int n,int a,int b,int c)
{
    if(n<=0)
        return -1;
    int res = max(max(getNum(n-a,a,b,c)),max(getNum(n-b,a,b,c)),max(getNum(n-c,a,b,c)));    
    if(res==-1)
        return -1;
    return res+1;    
}
int main()
{
    int n,a,b,c;
    cin>>n>>a>>b>>c;
    cout<<getNum(n,a,b,c);        
    return 0;
}