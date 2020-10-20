#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int fact(int n)
{
    if(n>0)
        return n*fact(n-1);
    else
        return 1;
}
int findRank(string &s)
{
    int length = s.length(),rank=0;
    int count[256]={0};
    int mal = fact(length);
    for(int i=0;i<length;i++)
        count[s[i]]=i;
    for(int i=1;i<256;i++)
        count[i]=count[i]+count[i-1];    
    for(int i=0;i<length;i++)
    {
        mal = mal/(length-i);
        rank = rank + count[s[i]-1]*mal;
        for(int j=s[i];j<256;j++)
            count[j]--;    
    }    
    return rank;

}

long int find_rank(string &s)
{
    string str=s;
    sort(s.begin(),s.end());
    long int i=1;
    do{
        if(s==str)
            break;
        i++;    
    }while(next_permutation(s.begin(),s.end()));
    return i;
}
int main()
{
    string s;
    cin>>s;
    cout<<find_rank(s)<<endl;
    return 0;
}