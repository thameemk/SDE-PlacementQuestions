# Variables

 A memory location associated with some name in order to store some form of data and retrieve it when required.

```c
// example
int num = 2; //single variable
int num_1, num_2;//multiple variable 

```

- Data type - type of data that a variable can store.
- Variable name - name of the variable given by the user.
- Value - value assigned to the variable by the user.

Three aspects of defining variable
- Variable declaration - tells the compiler about the existence of the variable with the given name and data type. No memory is allocated to a variable in the declaration.
- Variable definition - the compiler allocates some memory and some value to it. A defined variable will contain some random garbage value till it is not initialized.
- Variable initialization - the user assigns some meaningful value to the variable.

```c
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
```

Rules of naming variables
- Must only contain alphabets, digits, and underscore.
- Must start with an alphabet or an underscore only. It cannot start with a digit.
- No whitespace is allowed.
- Must not be any reserved word or keyword.
