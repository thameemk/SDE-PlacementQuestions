#include <stdio.h>

int main()
{
    // declaration with defnition
    int num;
    printf("defined number: %d\n", num);

    // initialization
    num = 10;

    // declaration + definition + initialization
    int num_2 = 20;

    printf("num after initialization: %d\n",num);
    printf("num_2: %d", num_2);

    return 0;
}