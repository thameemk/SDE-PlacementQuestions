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

void patternSearchManual(string s,string p)
{
    
}

int main()
{
    string s,p;
    cin>>s>>p;
    patternSearch(s,p);
    return 0;
}