import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        if (b<45) {
            a--;
            if (a<0) a=23;
            b = 60 - Math.abs(b-45);
        } else {
            b = b - 45;
        }

        System.out.println(a + " " + b);
    }
}