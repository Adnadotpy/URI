#include <stdio.h>

int main() {
    double A, B, C;
    printf("digite a primeira nota:\n");
    scanf("%lf", &A);
    printf("digite a segunda nota:\n");
    scanf("%lf", &B);
    printf("digite a terceira nota:\n");
    scanf("%lf", &C);
    double media = ((A*2) + (B*3) + (C*5))/10;
    printf("MEDIA = %.1lf", media);

    return 0;
}