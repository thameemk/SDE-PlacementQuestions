#include<iostream>
using namespace std;
int main()
{
    int array[] = {4,5,56,98};
    int array_size = sizeof(array)/sizeof(array[0]); 
    cout<<"Array before insertion\n";
    for(int i=0;i<array_size;i++)
        cout<<array[i]<<" ";
    //insert to an array
    int new_element = 40; 
    int new_element_index = 2;
    array_size = array_size+1;
    int j;
    for(j=2;j<array_size;j++)
        array[j+1] = array[j];
    array[j] = new_element;
    cout<<"Array after insertion\n";
    for(int i=0;i<array_size;i++)
        cout<<array[i]<<" ";
    return 0;    
}