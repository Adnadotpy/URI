#include <stdio.h>

int main() {
    int func, horas; // numero do funcionario, horas trabalhadas, valor por hora
    double valor;
    printf("digite o numero do funcionario:\n");
    scanf("%d", &func);
    printf("digite o numero de horas trabalhadas:\n");
    scanf("%d", &horas);
    printf("digite o valor recebido por hora:\n");
    scanf("%f", &valor);
    double salario = horas*valor;
    printf("NUMBER = %d\n", func);
    printf("SALARY = U$ %.2f\n", salario);

    return 0;
}