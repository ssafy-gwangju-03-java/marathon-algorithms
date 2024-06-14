import java.util.Arrays;
import java.util.Scanner;

public class 정하림_14550 {
    static int N, S, T;
    static int[] board;
    static int maxRevenue;
    static int[][] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            N = sc.nextInt();
            if (N == 0) break;

            S = sc.nextInt();
            T = sc.nextInt();

            board = new int[N + 2];
            for (int i = 1; i <= N; i++) {
                board[i] = sc.nextInt();
            }

            dp = new int[T + 1][N + 2];
            for (int i = 0; i < T+1; i++) {
                Arrays.fill(dp[i], -10000 * 201);
            }
            dp[0][0] = 0;

//           mario(0, 0, 0); // DFS 시간 초과

            for (int t = 0; t < T; t++) {
                for (int i = 0; i <= N + 1; i++) {
                    if (dp[t][i] == -10000 * 201) continue;
                    for (int s = 1; s <= S; s++) {
                        int next = i + s;
                        if (next > N + 1) break;
                        dp[t + 1][next] = Math.max(dp[t + 1][next], dp[t][i] + board[next]);
                    }
                }
            }

            maxRevenue = -10000 * 201;
            for (int t = 0; t <= T; t++) {
                maxRevenue = Math.max(maxRevenue, dp[t][N + 1]);
            }

            System.out.println(maxRevenue);
        }
    }
//    private static void mario(int current, int revenue, int count) {
//        if (current == N + 1) {
//            maxRevenue = Math.max(maxRevenue, revenue);
//            return;
//        }
//
//        if (count == T) return;
//
//        if (dp[count][current] > revenue) {
//            return;
//        } else {
//            dp[count][current] = revenue;
//        }
//
//        for (int i = 1; i <= S; i++) {
//            if (current + i > N + 1) break;
//            mario(current + i, revenue + board[current + i], count + 1);
//        }
//    }
}
