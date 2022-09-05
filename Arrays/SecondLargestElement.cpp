#include <iostream>
using namespace std;
int getSecondLarge(int array[],int array_size)
{
    int res=-1,largest=0;
    for(int i=0;i<array_size;i++)
    {
        if(array[i]>array[largest])
        {
            res=largest;
            largest = i;
        }
        else if(array[i]!=array[largest])
        {
            if(res==-1 || array[i]>array[res])
                res = i;
        }
    }
    return res;
}
int main()
{
    int arr[]={9,7,10,5,8};
    int array_size=sizeof(arr)/sizeof(arr[0]);
    cout<<"The second larest element is at: "<<getSecondLarge(arr,array_size)<<"\n";
    return 0;
}