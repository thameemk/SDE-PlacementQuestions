#include<iostream>
using namespace std;
int main(){
    int i,n,q,arr[1000];
    int que[3];    
    cin>>n>>q;
    for(i=0;i<n;i++){
        cin>>arr[i];
    }
    while(q--){
        int sum=0;
        for(i=0;i<3;i++){
            cin>>que[i];            
        }
        if(que[0]==1){
            arr[que[1]]=que[2];
        }
        else{
            for(int j=que[1];j<=que[2];j++){
                sum = sum + arr[j];
            }
            cout<<sum<<"\n";
        }       
    }
}
