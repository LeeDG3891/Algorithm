import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] array = new int[3];
        int count = 0;
        int sum = 0;

        for (int i=0; i<3; i++) {
            int a = Integer.parseInt(br.readLine());

            array[i] = a;
            if (array[i] == 60) count++;
            sum += array[i];
        }

        if (count == 3) {
            System.out.println("Equilateral");
            return;
        }
        if (sum != 180) {
            System.out.println("Error");
            return;
        }
        if (sum == 180 && array[0] == array[1] || array[0] == array[2] || array[1] == array[2]) {
            System.out.println("Isosceles");
        }
        if (sum == 180 && array[0] != array[1] && array[0] != array[2] && array[1] != array[2]) {
            System.out.println("Scalene");
        }

    }
}