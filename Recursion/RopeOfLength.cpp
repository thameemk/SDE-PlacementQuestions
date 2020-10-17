#include<iostream>
#include<algorithm>
// using namespace std;

// template <class T>
// T max(const T& t1, const T& t2, const T& t3)
// {
//     return t1 < t2 ? t2 : t1;
// }

int getNum(int n,int a,int b,int c)
{
    if(n<=0)
        return -1;
    int res = std::max(max(getNum(n-a,a,b,c)),max(getNum(n-b,a,b,c)),max(getNum(n-c,a,b,c)));    
    if(res==-1)
        return -1;
    return res+1;    
}
int main()
{
    int n,a,b,c;
    cin>>n>>a>>b>>c;
    cout<<getNum(n,a,b,c);        
    return 0;
}