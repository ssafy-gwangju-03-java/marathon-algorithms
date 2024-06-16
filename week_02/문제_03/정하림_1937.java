import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 정하림_1937 {
    static int n;
    static int[][] bamboo;
    static int[][] dp;
    static boolean[][] visited;
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        bamboo = new int[n][n];


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                bamboo[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp = new int[n][n];
        visited = new boolean[n][n];
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, panda(i, j));
            }
        }
        System.out.println(ans);
/*        for (int i = 0; i < n; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }*/

    }

    private static int panda(int r, int c) {
        int cnt = 1;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (0 <= nr && nr < n && 0 <= nc && nc < n && bamboo[r][c] < bamboo[nr][nc]) {
                if (visited[nr][nc]) {
                    cnt = Math.max(cnt, dp[nr][nc] + 1);
                } else {
                    cnt = Math.max(cnt, panda(nr, nc) + 1);
                    visited[nr][nc] = true;
                }
            }

        }
        dp[r][c] = cnt;
        return cnt;
    }

}
