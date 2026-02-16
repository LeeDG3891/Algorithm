import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            String s = br.readLine();
            int j = s.length()-1;
            sb.append(s.charAt(0)).append(s.charAt(j)).append("\n");
        }

        System.out.print(sb);
    }
}