#include <iostream>
using namespace std;
int main(){
	string s;
	int flag=0;
	cin>>s;	
	for(int i=0;i<s.length();i++){	
		if(s[i]!=s[s.length()-i-1])
		{
			flag=1;
			break;
		}
	}
	if(flag==0){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
	return 0;
}
