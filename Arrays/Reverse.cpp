#include<iostream>
using namespace std;
int new_array[] = {4,5,0,98};

void printArray(int arr[],int array_size)
{
     for(int i=0;i<array_size;i++)
        cout<<arr[i]<<" ";
}

void reverse(int arr[],int array_size)
{
    int i=0,n=array_size-1;
    while(i<n)
    {
        swap(arr[i],arr[n]);
        i++;
        n--;
    }
}
int main()
{   
    int array_size = sizeof(new_array)/sizeof(new_array[0]); 
    cout<<"Before reverse\n";
    printArray(new_array,array_size);
    cout<<"\nAfter reverse\n";
    reverse(new_array,array_size);
    printArray(new_array,array_size);
    return 0;    
}