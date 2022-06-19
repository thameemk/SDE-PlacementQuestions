#include<iostream>
using namespace std;
int new_array[] = {4,5,56,98};
void printArray(int arr[],int array_size)
{
     for(int i=0;i<array_size;i++)
        cout<<arr[i]<<" ";
}

void insertElement(int arr[],int new_element,int index,int array_size)
{    
    int j;
    for(j=array_size-1;j>index;j--)
        arr[j] = arr[j-1];
    arr[index] = new_element;
}

int main()
{  
    int array_size = sizeof(new_array)/sizeof(new_array[0]); 
    cout<<"Array before insertion\n";
    printArray(new_array,array_size);
    array_size = array_size+1;
    insertElement(new_array,40,2,array_size);
    cout<<"\nArray after insertion\n";
    printArray(new_array,array_size);
    return 0;    
}