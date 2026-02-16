import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        float[] arr = new float[n];
        float max = Integer.MIN_VALUE;
        float result = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());

            if(arr[i] > max) max = arr[i];
        }

        for (int i=0; i<n; i++) {
            result += arr[i]/max*100;
        }

        result /= n;
        System.out.println(result);

    }
}