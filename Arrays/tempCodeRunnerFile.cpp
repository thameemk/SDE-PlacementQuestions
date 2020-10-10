#include<iostream>
using namespace std;
int main()
{
    int array[] = {4,5,56,98};
    int array_size = sizeof(array)/sizeof(array[0]); 
    for(int i=0;i<array_size;i++)
        cout<<array[i]<<"\n";
    return 0;    
}