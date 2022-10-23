import java.util.Scanner;

class Maior {
  public static void main(String[] args) {
   Scanner leia = new Scanner(System.in);
    int a, b, c;
    a = leia.nextInt();
    b = leia.nextInt();
    c = leia.nextInt();
    int d = (a+b+Math.abs(a-b))/2;
    d = (d+c+Math.abs(d-c))/2;
    System.out.printf("%d eh o maior%n", d);
  }
}