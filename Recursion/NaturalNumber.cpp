#include<iostream>
using namespace std;
void printNumReverse(int n)
{
    //reverse order
    if(n==0)
        return;
    cout<<n<<" ";
    printNumReverse(n-1);
}
void printNum(int n,int k)
{
    if(k>n)
        return;
    cout<<k<<" ";
    printNum(n,k+1);
}
int main()
{
    int num;
    cout<<"\nEnter a number: ";        
    cin>>num;   
    printNumReverse(num);
    cout<<endl;
    printNum(num,1);
    return 0;
}