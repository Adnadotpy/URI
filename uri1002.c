#include <stdio.h>

int main() {
    double raio, n = 3.14159;
    printf("digite o valor do raio: \n");
    scanf("%lf", &raio); // lf = long float
    double area = n*raio*raio;
    printf("A= %.4lf", area);

    return 0;
}