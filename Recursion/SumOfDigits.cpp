#include<iostream>
using namespace std;
int sumofdigits(int n)
{
    if(n<10)
        return n;
    return n%10+sumofdigits(n/10);    
}
int main()
{
    int n;
    cout<<"\nEnter a nmber: ";        
    cin>>n;
    cout<<sumofdigits(n);
    return 0;
}