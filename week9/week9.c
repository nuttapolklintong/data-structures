#include <stdio.h>

int calculate(int a, int b, int c, int d, int *sum, int *diff, int *mul, int *div){

    *sum = a + b + c + d;
    *diff = a - b - c - d;
    *mul = a * b * c * d;
    *div = ((a / b) / c) / d;
}

int main(){
    int w,x,y,z;
    int s, d, m, div;
    scanf("Press Input data : ");
    calculate(w, x, y, z, &s, &d, &m, &div);
    printf("Sum = %d, Difference = %d, Multi=%d, Div =%d\n", s, d, m, div);

    return 0;
}