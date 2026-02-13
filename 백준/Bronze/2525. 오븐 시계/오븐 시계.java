import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        if (b+c>=60) {
            a = a + ((b + c) / 60);
            a %= 24;
            b = (b + c) % 60;
        } else b = b + c;

        System.out.println(a + " " + b);
    }
}