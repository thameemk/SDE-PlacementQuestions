#include<iostream>
#include<algorithm>
using namespace std;

void patternSearch(string s,string p)
{   
    int flag = s.find(p);
    while(flag!=string::npos)
    {
        cout<<"Pattern found at "<<flag<<"\n";
        flag = s.find(p,flag+1);
    }
}


// Naive Algorithm
void patternSearchManual(string s,string p)
{
    for(int i=0;i<=s.length()-p.length();i++)
    {
        int j;
        for(j=0;j<p.length();j++)
        {
            if(s[i+j]!=p[j])
                break;
        }
        if(j==p.length())
             cout<<"Pattern found at "<<i<<"\n";
    }
}

int main()
{
    string s,p;
    cin>>s>>p;
    patternSearch(s,p);
    cout<<"--------------------\n";
    patternSearchManual(s,p);
    return 0;
}