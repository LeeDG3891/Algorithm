import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int n = Integer.parseInt(br.readLine());
            int sum = 0;

            if (n == -1) break;

            for (int i=1; i<n; i++) {
                if (n % i == 0) {
                    sum += i;
                }
            }

            StringBuilder sb = new StringBuilder();

            if(sum == n) {
                sb.append(n).append(" = ");
                for (int i=1; i<n; i++) {
                    if (n % i == 0) {
                        sb.append(i).append(" + ");
                    }
                }
                sb.setLength(sb.length()-3);
                System.out.println(sb);
            }
            else System.out.println(n + " is NOT perfect.");
        }
    }
}