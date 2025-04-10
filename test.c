#include <stdio.h>
#define PI 3.14

// This is a single-line comment
int main() {
    /* This is a multi-line
       comment */
    int a = 10, b = 20;
    float result;

    result = a + b * 3.14; // Arithmetic operation
    if (a == b || a < b) { // Relational and logical operators
        printf("a is less than or equal to b\n");
    } else {
        printf("a is greater than b\n");
    }

    return 0;
}
