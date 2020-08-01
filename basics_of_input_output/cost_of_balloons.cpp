#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        float g,p,total=0;
        int n;
        cin>>g>>p;
        cin>>n;
        float sumg=0,sump=0;
        while(n--){
            int i,j;
            cin>>i>>j;
            sumg = sumg + i;            
            sump = sump + j;            
        }
        if(sumg>sump){
            if(g>p){
                total = sumg*p + sump*g;               
            }
            else{
                total = sumg*g + sump*p; 
            }
        }
        else{
            if(g>p){
                total = sump*p + sumg*g;               
            }
            else{
                total = sump*g + sumg*p; 
            }
        }
        cout<<total<<"\n";
    }
    return 0;
}
