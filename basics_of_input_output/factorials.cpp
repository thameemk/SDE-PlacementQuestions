#include <iostream>
using namespace std;
int main(){
    int n,temp=1;
    cin>>n;
    while(n>0){
        temp = temp*n;
        n--;
    }
    cout<<temp;
    return 0;
}
