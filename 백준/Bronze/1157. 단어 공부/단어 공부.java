import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine().toUpperCase();
        int[] count = new int[26];
        int max = Integer.MIN_VALUE;
        char result = '?';

        for (int i=0; i<s.length(); i++) {
            count[s.charAt(i) - 'A']++;
        }

        for (int i=0; i<count.length; i++) {
            if (count[i] > max) {
                max = count[i];
                result = (char)(i + 'A');
            }
            else if (count[i] == max) result = '?';
        }
        System.out.println(result);

    }
}