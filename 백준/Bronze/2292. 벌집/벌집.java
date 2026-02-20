import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int max = 1;
        int floor = 1;

        while (n > max) {
            max += 6 * floor;
            floor++;
        }

        System.out.println(floor);
    }
}