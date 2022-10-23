/*import java.util.Scanner;

class Media {
    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
        float A, B;
        double media;
        A = leia.nextFloat();
        B = leia.nextFloat();
        media = ((A * 3.5) + (B * 7.5))/11;
        media = leia.nextDouble();
        System.out.printf("%5.f MEDIA = %n" + media);
    }
} */

import java.util.Scanner;

class Uri1005 {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        double a = leitor.nextDouble();
        double b = leitor.nextDouble();
        double media = ((3.5 * a) + (7.5 * b))/11;
        System.out.println(String.format("MEDIA = %.5f" , media));
    }
}