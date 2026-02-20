import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String n = st.nextToken();
        int b = Integer.parseInt(st.nextToken());
        int result = 0;

        for (int i=0; i<n.length(); i++) {
            int value;

            if (n.charAt(i) >= '0' && n.charAt(i) <= '9') value = n.charAt(i) - '0';
            else value = n.charAt(i) - 'A' + 10;

            result = result * b + value;
        }
        System.out.println(result);
    }
}