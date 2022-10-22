import java.util.Scanner;

class Fatorial {	
    public static void main (String[] args) {
        Scanner leia = new Scanner(System.in);
        int N = leia.nextInt();
        int fatorial = 1;
        for (int i = 1; i <= N; i++) {
        	fatorial *= i;
        }
        System.out.println(fatorial);
    }
}