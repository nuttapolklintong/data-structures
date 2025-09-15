#include <stdio.h>

void rotate3(int *x, int *y, int *z) {
    int temp = *x;  
    *x = *z;         
    *z = *y;
    *y = temp;
}

int main() {
    int a = 10, b = 20, c = 30;

    printf("Before rotation: x = %d, y = %d, z = %d\n", a, b, c);

    rotate3(&a, &b, &c);

    printf("After rotation: x = %d, y = %d, z = %d\n", a, b, c);

    return 0;
}