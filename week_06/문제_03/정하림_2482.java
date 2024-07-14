import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 정하림_2482 {
    static int N, K;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        if (N / 2 < K)  {
            System.out.println(0);
            return;
        }
        dp = new int[N + 1][K + 1];
        for (int i = 1; i <= N; i++) {
            dp[i][0] = 1;
            dp[i][1] = i;
        }
        for (int i = 2; i < N; i++) {
            for (int j = 2; j <= K; j++) {
                dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003;
            }
        }
        System.out.println((dp[N-3][K-1] + dp[N-1][K]) % 1000000003);
    }
}