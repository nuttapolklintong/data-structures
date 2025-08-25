#include <stdio.h>


int swap(int *a, int *b, int *c){
    
    int temp = *a;
    *a = *b;
    *b = *c;
    *c = temp;

}

int main(){
    
    int x , y , z ;
    
    printf("Input data x and y and z : ");
    scanf("%d %d %d", &x, &y, &z);
    
    printf("Before Swap: x=%d, y=%d, z=%d\n", x, y, z);
    
    swap(&x, &y, &z);
    
    printf("After Swap: x=%d, y=%d, z=%d\n", x, y, z);

    return 0;
}