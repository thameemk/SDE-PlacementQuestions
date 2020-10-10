#include<iostream>
using namespace std;
int main()
{
    int array[] = {5,7,8,9,10};
    int search_element = 9;
    int array_size = sizeof(array)/sizeof(array[0]);
    for(int i=0;i<array_size;i++) 
    {
        if(array[i]==search_element)
            cout<<"Element found at index: "<<i<<"\n";
    }
    return 0;
}