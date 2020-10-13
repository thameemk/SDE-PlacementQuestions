#include<iostream>
using namespace std;
int fact(int n,int k=1)
{
    if(n>0)
        return fact(n-1,n*k);
    else
        return k;
}
int main()
{
    int num;
    cout<<"\nEnter a number: ";        
    cin>>num;
    cout<<"\n Factorial = "<<fact(num)<<endl;
    return 0;
}