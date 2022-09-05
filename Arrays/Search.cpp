#include<iostream>
using namespace std;
void search(int array[],int search_element)
{
    int array_size = sizeof(array)/sizeof(array[0]);
    int res=-1,i;
    for(i=0;i<array_size;i++) 
    {
        if(array[i]==search_element)
            res = i;         
    }
    if(res!=-1)
       cout<<"Element fount at: "<<i<<"\n";
    else
        cout<<"Element not found\n";
}
int main()
{
    int arr[] = {5,7,8,9,10};
    int search_element = 9;
    search(arr,search_element);   
    return 0;
}