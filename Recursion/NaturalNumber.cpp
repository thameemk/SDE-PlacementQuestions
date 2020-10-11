#include<iostream>
using namespace std;
void printNum(int n)
{
    if(n==0)
        return;
    cout<<n<<" ";
    printNum(n-1);
}
int main()
{
    int num;
    cout<<"\nEnter a number: ";        
    cin>>num;   
    printNum(num);
    return 0;
}