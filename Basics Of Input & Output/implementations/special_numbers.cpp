#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> g;
void f(long long v) {
        if (v > n) return;
        if (v > 0) g.push_back(v);
        f(10*v + 4);
        f(10*v + 7);
}
int main() {
        cin >> n;
        f(0);
        int result = 0;
        for (int i = 0; i < (int)g.size(); ++i)
                for (int j = i + 1; j < (int)g.size(); ++j)
                        if (__gcd(g[i], g[j]) == 1)
                                ++result;
        cout << result << '\n';
        return 0;
}
