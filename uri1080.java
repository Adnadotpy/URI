import java.util.Scanner;

class MaiorPosicao {
    public static void main(String[] args){
        Scanner leia = new Scanner(System.in);
        int a, maior, pmaior;
        maior = 0;
        pmaior = 1;
        for (int i = 1; i <= 100; i++) {
            a = leia.nextInt();
            if (i == 1) {
                maior = a;
                pmaior = 1;
            }
            else if (a > maior) {
                maior = a;
                pmaior = i;
            }
        }
        System.out.println(maior);
        System.out.println(pmaior);
    }
}