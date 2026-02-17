import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String a = st.nextToken();
        String b = st.nextToken();

        StringBuilder sba = new StringBuilder();
        StringBuilder sbb = new StringBuilder();

        for (int i=a.length()-1; i>=0; i--) {
            sba.append(a.charAt(i));
        }

        for (int i=b.length()-1; i>=0; i--) {
            sbb.append(b.charAt(i));
        }

        String reverse1 = sba.toString();
        String reverse2 = sbb.toString();

        int num1 = Integer.parseInt(reverse1);
        int num2 = Integer.parseInt(reverse2);

        System.out.println(num1 > num2 ? num1 : num2);
    }
}