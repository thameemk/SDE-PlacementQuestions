#include<iostream>
using namespace std;
int new_array[] = {4,5,0,98};

void printArray(int arr[],int array_size)
{
     for(int i=0;i<array_size;i++)
        cout<<arr[i]<<" ";
}

void leftRotate(int arr[],int array_size,int count)
{
    int temp = arr[0];
    for(int i=0;i<array_size;i=i+count)
    {
        arr[i]=arr[i+1];
    }       
    arr[array_size-1]=temp;        
}
int main()
{   
    int array_size = sizeof(new_array)/sizeof(new_array[0]); 
    cout<<"Before rotate\n";
    printArray(new_array,array_size);
    cout<<"\nAfter rotate\n";
    leftRotate(new_array,array_size,1);
    printArray(new_array,array_size);
    return 0;    
}