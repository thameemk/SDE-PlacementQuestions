#include<iostream>
using namespace std;
int getLarge(int array[], int array_size)
{
    int res=array[0];   
    for(int i=0;i<array_size;i++)
    {
        if(array[res]<array[i])
            res=i;
    }
    return res;
}
int main()
{
    int arr[]={9,7,10,5,8};
    int array_size=sizeof(arr)/sizeof(arr[0]);
    cout<<"The larest element is at: "<<getLarge(arr,array_size)<<"\n";
    return 0;
}