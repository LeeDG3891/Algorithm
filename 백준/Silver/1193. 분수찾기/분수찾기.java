import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        int diagonal = 1;
        int sum = 0;

        while (sum + diagonal < x) {
            sum += diagonal;
            diagonal++;
        }

        int position = x - sum;
        int num1, num2;

        if (diagonal % 2 == 0) {
            num1 = position;
            num2 = diagonal + 1 - position;
        } else {
            num2 = position;
            num1 = diagonal + 1 - position;
        }

        System.out.println(num1 + "/" + num2);
    }
}