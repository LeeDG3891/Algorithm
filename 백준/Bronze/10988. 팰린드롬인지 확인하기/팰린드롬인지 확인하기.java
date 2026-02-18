import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String palindrome = br.readLine();
        String s = "";

        for (int i=palindrome.length()-1; i>=0; i--) {
            s += palindrome.charAt(i);
        }

        System.out.println(palindrome.equals(s) ? 1 : 0);

        /*
        String reverse = new StringBuilder(palindrome).reverse().toString();
        System.out.println(palindrome.equals(reverse) ? 1 : 0);
        */

    }
}