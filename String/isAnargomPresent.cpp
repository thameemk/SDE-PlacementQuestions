#include<iostream>
#include<algorithm>
using namespace std;
bool areSame(int c1[],int c2[])
{   
    for (int i = 0; i <256 ; i++) 
        if (c1[i] != c2[i]) 
            return false;
    return true;         
}
bool isAnargomPresent(string s1,string s2)
{
    int count1[256]={0},count2[256]={0};
    for(int i=0;i<s2.length();i++)
    {
        count1[s1[i]]++;
        count2[s2[i]]++;
    }
    for(int i=s2.length();i<s1.length();i++){
        if(areSame(count1,count2))
            return true;
        count1[s1[i]]++;
        count1[s1[i-s2.length()]]--;
    }
    return false;
}
int main()
{
    string s1,s2;
    cin>>s1>>s2;
    cout<<isAnargomPresent(s1,s2)<<"\n";
    return 0;
}