#include<iostream>
using namespace std;
int getLarge(int array[])
{
    int res=0;
    int array_size=sizeof(array)/sizeof(array[0]);
    for(int i=0;i<array_size;i++)
    {
        if(array[res]<array[i])
            res=i;
    }
    return res;
}
int main()
{
    int arr[]={9,7,10.5,8};
    cout<<"The larest element is at: "<<getLarge(arr)<<"\n";
    return 0;
}