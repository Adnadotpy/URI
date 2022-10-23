import java.util.Scanner;

class Diferenca {
    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
        int A, B, C, D, DIFERENCA;
        A = leia.nextInt();
        B = leia.nextInt();
        C = leia.nextInt();
        D = leia.nextInt();
        DIFERENCA = (A * B - C * D);
        System.out.println("DIFERENCA = " + DIFERENCA);
    }
}