#include<iostream>
using namespace std;
int main(){
    int t,a,b,count;
    cin>>t;
    while(t--){
        cin>>a>>b;
        if(a<b){
            count=b/a;
        }
        else{
            count=a/b;
        } 
        cout<<count<<"\n";   
    }
    return 0;
}
