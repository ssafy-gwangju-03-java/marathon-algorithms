import java.io.*;

public class 김가람_1011 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int t = 0; t < T; t++) {
            String[] input = br.readLine().split(" ");
            int x = Integer.parseInt(input[0]);
            int y = Integer.parseInt(input[1]);

            long distance = y - x;
            long max = (long) Math.sqrt(distance);

            // 참고 : https://st-lab.tistory.com/79
            if (max * max == distance) {
                sb.append(2 * max - 1).append("\n");
            } else if (distance <= max * max + max) {
                sb.append(2 * max).append("\n");
            } else {
                sb.append(2 * max + 1).append("\n");
            }
        }

        System.out.print(sb.toString());
    }
}