#include<iostream>
using namespace std;
int subString(string str, string sub)
{
    int l1 = str.length();
    int l2 = sub.length(); 
    int total=0,i; 
    for(i=0;i<l1;)
    {
        int j=0,count=0;
        while(str[i]==sub[j]){
            count++;
            i++;
            j++;
        }
        if(count==l2)
        {
            total++;
            count=0;
        }
    }
    return total;
}
int main()
{
    string a,b;
    cout<<"Enter string:\n";
    cin>>a;
    cout<<"Enter substring:\n";
    cin>>b;
    subString(a,b);
    return 0;
}