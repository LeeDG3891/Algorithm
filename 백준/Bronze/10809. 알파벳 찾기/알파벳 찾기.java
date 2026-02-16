import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s = br.readLine();

        for (char c='a'; c<='z'; c++) {
            sb.append(s.indexOf(c)).append(" ");
        }
        if (sb.length()>=0) sb.setLength(sb.length()-1);
        System.out.print(sb);
    }
}