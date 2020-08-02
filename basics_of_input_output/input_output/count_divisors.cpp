#include <iostream>
using namespace std;
int main(){
    int l,r,k,temp=0;
    cin>>l>>r>>k; 
    for(;l<=r;l++){
        if(l%k==0){
            temp+=1;
        }
    }
    cout<<temp;
    return 0;
}
