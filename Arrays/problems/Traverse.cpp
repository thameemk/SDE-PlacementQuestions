#include<iostream>
using namespace std;

void printArray(int arr[],int array_size)
{
     for(int i=0;i<array_size;i++)
        cout<<arr[i]<<"\n";
}

int main()
{
    int array[] = {4,5,56,98};
    int array_size = sizeof(array)/sizeof(array[0]); 
    printArray(array,array_size);
    return 0;    
}