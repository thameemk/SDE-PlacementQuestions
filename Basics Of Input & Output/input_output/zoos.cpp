#include <iostream>
#include <cstring>
#include <string>
using namespace std;
int main()
{
	string str;
	char str_arr[100];
	int x=0,y=0;	
	getline(cin,str);
	int length = str.size();
	strcpy(str_arr,str.c_str());
	for(int i=0;i<length;i++)
	{
		if(str_arr[i]=='z')
		{
			x++;
		}
		else if(str_arr[i]=='o')
		{
			y++;
		}
	}
	if(2*x==y)
	{
		cout<<"Yes\n";
	}
	else
	{
		cout<<"No\n";
	}
	return 0;
}
