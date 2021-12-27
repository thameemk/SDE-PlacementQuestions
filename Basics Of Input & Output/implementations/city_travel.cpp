#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;
int main()
{
    long long int s,x,n,sum=0,d=0,j=0;
    cin>>s>>x>>n;
    vector<pair<long long int ,long long int>>v(n);
    for(int i=0;i<n;i++)
        cin>>v[i].first>>v[i].second;
    sort(v.begin(),v.end());
    while(sum<s)
    {
        d++;
        if(d==(v[j].first))
        {
            sum=sum+v[j].second;        
            j++;
        }
        else
            sum=sum+x;
    }
    cout<<d<<endl;
    return 0;
}