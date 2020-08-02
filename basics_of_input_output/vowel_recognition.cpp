#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    string s;
    while(t--){
        long int count=0;
        cin>>s;
        long int l = s.length();
        for(int k=0;k<l;k++){                             
                    if((s[k] == 'a' || s[k] == 'e' || s[k] == 'i' || s[k] == 'o' || s[k] == 'u' || s[k] == 'A' || s[k] == 'E' || s[k] == 'I' || s[k] == 'O' || s[k] == 'U')){
                         count = count + (l - k) * (k+1);
                    }
                }                                   
        cout<<count<<"\n";
    }
    return 0;
}
