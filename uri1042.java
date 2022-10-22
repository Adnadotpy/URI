import java.util.Scanner;

class SortSimples {
    public static void main(String[] args){
        Scanner leia = new Scanner(System.in);
        int n1, n2, n3;
        n1 = leia.nextInt();
        n2 = leia.nextInt();
        n3 = leia.nextInt();
        if (n1 < n2 && n1 < n3) { //se n1 for menor q n2 e n3 -> printar: n1. se n2 for menor n3, printar: n2, n3. se não: n3, n2
            System.out.println(n1);
            if (n2 < n3) {
                System.out.println(n2);
                System.out.println(n3); 
            }
            else {
                System.out.println(n3);
                System.out.println(n2);
            }
        }
        else if (n2 < n3) { // se n2 for menor que n3, printar n2. se n1 for menor que n3, printar n1, n3. se não, printar n3, n1
            System.out.println(n2);
            if (n1 < n3) {
                System.out.println(n1);
                System.out.println(n3);
            }
            else {
                System.out.println(n3);
                System.out.println(n1);
            }
        }
        else {
            System.out.println(n3); // 
            if (n1 < n2) {
                System.out.println(n1);
                System.out.println(n2);
            }
            else {
                System.out.println(n2);
                System.out.println(n1);
            }
        }
        System.out.println(" "); // print na sequencia que foram escritos
        System.out.println(n1);
        System.out.println(n2);
        System.out.println(n3);
    }
}