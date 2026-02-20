import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] array = new int[9][9];
        int max = Integer.MIN_VALUE;

        for (int i=0; i<9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j=0; j<9; j++) {
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (array[i][j] > max) max = array[i][j];
            }
        }

        System.out.println(max);

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (array[i][j] == max) System.out.println((i+1) + " " + (j+1));
            }
        }
    }
}