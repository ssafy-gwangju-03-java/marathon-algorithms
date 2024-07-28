import java.util.Scanner;

public class 정하림_11049 {
    static int N;
    static int[][] matrix;
    static int[][] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        matrix = new int[N][2];
        dp = new int[N][N];

        for (int i = 0; i < N; i++) {
            matrix[i][0] = sc.nextInt();
            matrix[i][1] = sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dp[i][j] = (i == j) ? 0 : Integer.MAX_VALUE; // 대각
            }
        }


        for (int len = 1; len < N; len++) {
            for (int i = 0; i + len < N; i++) {
                int j = i + len;
                for (int mid = i; mid < j; mid++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][mid] + dp[mid + 1][j]
                            + matrix[i][0] * matrix[mid][1] * matrix[j][1]);
                }
            }
        }

        System.out.println(dp[0][N - 1]);
    }
}