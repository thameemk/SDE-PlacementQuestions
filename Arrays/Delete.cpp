#include<iostream>
using namespace std;
int main()
{
    int array[] = {4,5,56,98};
    int array_size = sizeof(array)/sizeof(array[0]); 
    cout<<"Array before deletion\n";
    for(int i=0;i<array_size;i++)
        cout<<array[i]<<" ";
    //delete an element from array
    int del_element = 40; 
    int j;
    for(j=0;j<array_size;j++){
        if(array[j]==del_element)
            break;
    }
    array_size = array_size-1;   
    for(j=2;j<array_size;j++)
        array[j-1] = array[j];
    cout<<"Array after deletion\n";
    for(int i=0;i<array_size;i++)
        cout<<array[i]<<" ";
    return 0;    
}