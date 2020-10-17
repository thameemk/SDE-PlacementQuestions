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
            cout << endl;
        }
    }
}
int main()
{
    string s;
    cout<<"Enter s string:";
    cin>>s;
    substring(s);
    return 0;
}