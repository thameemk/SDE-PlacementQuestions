#include <iostream>

using namespace std;

int main()

{

    int t,n;

    cin>>t;

    while(t--)

    {

        cin>>n;

        if(n%12==0||n%12==1 || n%12==6||n%12==7)

        {

            if(n%12==0)

            {

                cout<<n-11<<" WS\n";

            }

            else if(n%12==1)

            {

                cout<<n+11<<" WS\n";

            }

            else if(n%12==6)

            {

                cout<<n+1<<" WS\n";

            }

            else if(n%12==7)

            {

                cout<<n-1<<" WS\n";

            }

        }

        else if(n%12==2||n%12==5 || n%12==8||n%12==11)

        {

            if(n%12==2)

            {

                cout<<n+9<<" MS\n";

            }

            else if(n%12==5)

            {

                cout<<n+3<<" MS\n";

            }

            else if(n%12==8)

            {

                cout<<n-3<<" MS\n";

            }

            else if(n%12==11)

            {

                cout<<n-9<<" MS\n";

            }

        }

        else if(n%12==3||n%12==4 || n%12==9||n%12==10)

        {

            if(n%12==3)

            {

                cout<<n+7<<" AS\n";

            }

            else if(n%12==4)

            {

                cout<<n+5<<" AS\n";

            }

            else if(n%12==9)

            {

                cout<<n-5<<" AS\n";

            }

            else if(n%12==10)

            {

                cout<<n-7<<" AS\n";

            }

        }                

    }



    return 0;

}
