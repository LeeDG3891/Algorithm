import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            String r = st.nextToken();


            for (int k=0; k<r.length(); k++) {
                for (int j=0; j<a; j++) {
                    sb.append(r.charAt(k));
                }
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}