#include<iostream>
using namespace std;
int main(){
    long long int t,l,r,s,i,j;
    cin>>t;
    while(t--){
        cin>>l>>r>>s;
        l = (l-1)/s+1;
        r=r/s;
        if(l>r){
            cout<<"-1 -1\n";
        }
        else{
            cout<<l<<" "<<r<<"\n";
        }
    }
    return 0;
}
