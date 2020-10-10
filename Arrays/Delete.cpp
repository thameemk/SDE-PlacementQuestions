#include<iostream>
using namespace std;
int new_array[] = {4,5,56,98};
void printArray(int arr[],int array_size)
{
     for(int i=0;i<array_size;i++)
        cout<<arr[i]<<" ";
}

void deleteElement(int arr[],int index,int array_size)
{    
    int j;
    for(j=index;j<array_size;j++)
        arr[j] = arr[j+1];   
}

int main()
{  
    int array_size = sizeof(new_array)/sizeof(new_array[0]); 
    cout<<"Array before deletion\n";
    printArray(new_array,array_size);
    array_size = array_size-1;
    deleteElement(new_array,2,array_size);
    cout<<"\nArray after deletion\n";
    printArray(new_array,array_size);
    return 0;    
}