#include <stdio.h>

int main() {
    double A, B;
    printf("digite a primeira nota:\n");
    scanf("%lf", &A);
    printf("digite a segunda nota:\n");
    scanf("%lf", &B);
    double media = ((A*3.5)+(B*7.5))/11;
    printf("MEDIA = %.5lf\n", media);

    return 0;
}