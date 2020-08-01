#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int l1,l2;
		string s1,s2;
		cin>>s1>>s2;
		l1 = s1.length();
		l2 = s2.length();
		int c=0;
		for(int i=0;i<l1;i++){
			for(int j=0;j<l2;j++){
				if(s1[i]==s2[j]){
					s2[j]=0;
					c++;
					break;
				}
			}
		}
		cout<<l1-c+l2-c<<"\n";
	}
	return 0;
}
