#include<iostream>
using namespace std;
int main(){
    string x;
    int k,temp=0;
    cin>>x>>k;
    for(int i=0;temp<k;i++){
        if(x[i]!='9'){
            x[i]='9';
            temp++;            
        }
    }
    cout<<x<<"\n";
    return 0;
}
