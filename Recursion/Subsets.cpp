#include <iostream>
using namespace std;
void substring(string s) //manual method
{    
    for (int i = 1; i <= s.length(); i++) 
    {    
        for (int j = 0; j <= s.length() - i; j++) 
        {            
            for (int k = j; k <= j+i-1; k++) 
                cout << s[k];             
            cout << " ";
        }
    }
}
void substringRecusrsion(string s,string current="",int i=0) //using recursion
{
    if(i==s.length()){
        cout<<current<<" ";return;
    }  
    substringRecusrsion(s,current,i+1);
    substringRecusrsion(s,current+s[i],i+1);        
}

int main()
{
    string s;
    cout<<"Enter s string:";
    cin>>s;
    // substring(s);
    substringRecusrsion(s);
    return 0;
}