#include <stdio.h>
  
int main()
{
    int a = 10, b = 4, res;
  
    printf("Post Increment and Decrement\n");
    // post-increment example:
    // res is assigned 10 only, a is not updated yet
    res = a++;
    printf("a is %d and res is %d\n", a,
           res); // a becomes 11 now
  
    // post-decrement example:
    // res is assigned 11 only, a is not updated yet
    res = a--;
    printf("a is %d and res is %d\n", a,
           res); // a becomes 10 now
  
    printf("\nPre Increment and Decrement\n");
    // pre-increment example:
    // res is assigned 11 now since
    // a is updated here itself
    res = ++a;
  
    // a and res have same values = 11
    printf("a is %d and res is %d\n", a, res);
  
    // pre-decrement example:
    // res is assigned 10 only since a is updated here
    // itself
    res = --a;
  
    // a and res have same values = 10
    printf("a is %d and res is %d\n", a, res);
  
    return 0;
}