#include <iostream>
#include <boost/multiprecision/cpp_int.hpp> 
using boost::multiprecision::cpp_int;
using namespace std;
int main(){
    cpp_int a,b;
    // long long int a,b;
    while(cin>>a>>b){               
        cout<<a+b<<"\n";
    }
    return 0;
}
