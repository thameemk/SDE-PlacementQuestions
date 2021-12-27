#include <iostream>
using namespace std;
int main(){
    string s;
    cin>>s;
    int l=s.length();
    for(int i=0;i<l;i++){
        if(isupper(s[i])){
            s[i]=tolower(s[i]);
        }
        else if(islower(s[i])){
            s[i] = toupper(s[i]);
        }
    }
    cout<<s;
    return 0;
}
