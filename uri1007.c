#include <stdio.h>

int main() {
    int A, B, C, D;
    printf("digite o valor de A:\n");
    scanf("%d", &A);
    printf("digite o valor de B:\n");
    scanf("%d", &B);
    printf("digite o valor de C:\n");
    scanf("%d", &C);
    printf("digite o valor de D:\n");
    scanf("%d", &D);
    int DIFERENCA = (A*B - C*D);
    printf("DIFERENCA = %d", DIFERENCA);

    return 0;
}