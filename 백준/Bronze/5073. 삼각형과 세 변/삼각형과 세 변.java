import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0 && b == 0 && c == 0) break;

            int[] array = {a, b, c};
            Arrays.sort(array);

            if (array[0] + array[1] <= array[2]) sb.append("Invalid").append("\n");
            else if (a == b && b == c) sb.append("Equilateral").append("\n");
            else if (a == b || a == c || b == c) sb.append("Isosceles").append("\n");
            else if (a != b && b != c) sb.append("Scalene").append("\n");
        }
        sb.setLength(sb.length()-1);
        System.out.println(sb);
    }
}