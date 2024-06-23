import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 정하림_1520 {
    static int N, M;
    static int[][] map, dp;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        dp = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }

        dfs(0,0, map[0][0]);

        System.out.println(dp[0][0]);
    }

    private static int dfs(int r, int c, int now) {
        if (r == N - 1 && c == M - 1) return 1; // 도착


        if (dp[r][c] != -1) return dp[r][c]; //
        else dp[r][c] = 0;

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            boolean inRange = (nr >= 0 && nr < N && nc >= 0 && nc < M);
            if (inRange && now > map[nr][nc]) {
                dp[r][c] += dfs(nr, nc, map[nr][nc]);
//                for (int i = 0; i < N; i++) {
//                    System.out.println(Arrays.toString(dp[i]));
//                }
//                System.out.println("----------------");
            }
        }
        return dp[r][c];
    }
}
