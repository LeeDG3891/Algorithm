import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int[] a = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i=0; i<n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        for (int i=0; i<n; i++) {
            if (a[i]<x) sb.append(a[i]).append(" ");
        }

        if(sb.length()>0) sb.setLength(sb.length()-1);
        System.out.print(sb);
    }
}