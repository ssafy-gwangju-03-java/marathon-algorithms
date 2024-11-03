import java.io.*;

public class 김가람_2293 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ipt = br.readLine().split(" ");

        int N = Integer.parseInt(ipt[0]);
        int K = Integer.parseInt(ipt[1]);

        int[] coin = new int[N];
        int[] memo = new int[K + 1];

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            coin[i] = num;
        }

        // 0원을 만드는 경우의 수는 1
        memo[0] = 1;

        // 각 동전을 사용하여 만들 수 있는 금액의 경우의 수 누적
        for (int i = 0; i < N; i++) {
            int curr = coin[i];
            for (int j = curr; j <= K; j++) {
                memo[j] = memo[j] + memo[j - curr];
            }
        }

        System.out.println(memo[K]);
    }
}