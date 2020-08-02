#include <iostream>
using namespace std;
int main(){
    int n;
    int arr[1000];
    long int product=1;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>arr[i];
        product = (product*arr[i])%1000000007;
    }
    cout<<product;
    return 0;
}
