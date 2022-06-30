#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string add_binary(string a, string b)
{
    int len_a = a.size() - 1;
    int len_b = b.size() - 1;
    int carry = 0;

    string sum;

    while (len_a >= 0 || len_b >= 0)
    {
        if (len_a >= 0)
        {
            // a[len_a] is a string and adding it with integer gives the ascii value. subtracting it with '0' gives the result
            carry = carry + a[len_a] - '0';
        }

        if (len_b >= 0)
        {
            carry = carry + b[len_b] - '0';
        }

        // push the ascii to string 'sum' convert it as the original text value

        sum.push_back((carry % 2) + '0');

        if (carry > 1)
            carry = 1;
        else
            carry = 0;

        len_a--;
        len_b--;
    }

    if (carry)
        sum.push_back((carry % 2) + '0');

    reverse(sum.begin(), sum.end());

    return sum;
}

int main()
{
    string a = "11";
    string b = "1";
    cout << "\n"
         << add_binary(a, b) << "\n";
    return 0;
}