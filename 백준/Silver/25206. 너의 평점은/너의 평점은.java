import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double totalscore = 0;
        double totalcredit = 0;

        for (int i=0; i<20; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String subject = st.nextToken();
            double credit = Double.parseDouble(st.nextToken());
            String grade = st.nextToken();
            double score = 0;

            if (grade.equals("P")) continue;

            if (grade.equals("A+")) score = 4.5;
            else if (grade.equals("A0")) score = 4.0;
            else if (grade.equals("B+")) score = 3.5;
            else if (grade.equals("B0")) score = 3.0;
            else if (grade.equals("C+")) score = 2.5;
            else if (grade.equals("C0")) score = 2.0;
            else if (grade.equals("D+")) score = 1.5;
            else if (grade.equals("D0")) score = 1.0;
            else score = 0;

            totalscore += credit * score;
            totalcredit += credit;
        }

        System.out.printf("%.6f",totalscore / totalcredit);
    }
}