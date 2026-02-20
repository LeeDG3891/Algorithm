import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        int[] array = {25, 10, 5, 1};

        for (int i=0; i<t; i++) {
            int a = Integer.parseInt(br.readLine());
            int[] result = new int[4];

            for (int j=0; j<array.length; j++) {
                result[j] = a / array[j];
                a = a % array[j];
                sb.append(result[j]).append(" ");
            }
            if (sb.length() > 0) sb.setLength(sb.length()-1);
            sb.append("\n");
        }
        System.out.print(sb);

    }
}