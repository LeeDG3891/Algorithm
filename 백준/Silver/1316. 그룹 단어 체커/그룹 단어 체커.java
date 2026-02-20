import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int count = 0;

        for (int i=0; i<n; i++) {
            String s = br.readLine();
            int j;

            for (j=1; j<s.length(); j++) {
                if (s.charAt(j) != s.charAt(j-1) && s.indexOf(s.charAt(j)) < j) break;
            }
            if (j==s.length()) count++;
        }

        System.out.println(count);
    }
}