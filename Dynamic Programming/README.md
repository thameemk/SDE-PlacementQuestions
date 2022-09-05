# Dynamic Programming

The programming method helps to efficiently solve problems that have overlapping sub-problems and optimal substructural property.

```cpp
// Recursion
int fibonacci(int n)
{
    if(n<=1)
        return n;
    return fibonacci(n-1)+fibonacci(n-2)
}

// Dynamic programming - Linear

f[0]=0;
f[1]=1;

for (int i=2;i<=n;i++)
{
    f[i]=f[i-1]+f[i-2];
}

return f[n];