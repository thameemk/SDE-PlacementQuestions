#include<iostream>
using namespace std;
int new_array[] = {4,5,0,98,0,7,0,1};
void printArray(int arr[],int array_size)
{
     for(int i=0;i<array_size;i++)
        cout<<arr[i]<<" ";
}
void moveZero(int arr[],int array_size)
{
    int temp=0;
    for(int i=0;i<array_size;i++)
    {
        if(arr[i]!=0)
        {
            swap(arr[i],arr[temp]);
            temp++;
        }
    }
}
int main()
{   
    int array_size = sizeof(new_array)/sizeof(new_array[0]); 
    cout<<"Before operation\n";
    printArray(new_array,array_size);
    cout<<"\nAfter operation\n";
    moveZero(new_array,array_size);
    printArray(new_array,array_size);
    return 0;    
}