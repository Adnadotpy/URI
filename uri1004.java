import java.util.Scanner;

class Produto {
    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
        int num1, num2, PROD;
        num1 = leia.nextInt();
        num2 = leia.nextInt();
        PROD = num1 * num2;
        System.out.println("PROD = " + PROD);
    }
}