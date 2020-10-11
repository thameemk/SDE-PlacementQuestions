#include<iostream>
using namespace std;
int fact(int n)
{
    if(n>0)
        return n*fact(n-1);
    else
        return 1;
}
int main()
{
    int num;
    cout<<"\nEnter a number: ";        
    cin>>num;
    cout<<"\n Factorial = "<<fact(num)<<endl;
    return 0;
}