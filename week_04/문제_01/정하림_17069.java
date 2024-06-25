import java.io.*;
import java.util.*;
import java.lang.*;

public class 정하림_17069 {
    static int N;
    static int[][] map;
    static long[][][] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        dp = new long[N][N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j][0] = -1;
                dp[i][j][1] = -1;
                dp[i][j][2] = -1;
            }
        }
        System.out.println(Math.max(pipe(0,1, 0), 0));
    }

    private static long pipe(int r, int c,  int d) { // 끝 r, c, 방향 d
        if (r == N-1 && c == N-1) return 1; // 끝

        if (dp[r][c][d] != -1) return dp[r][c][d]; // 방문 누적
        dp[r][c][d] = 0; // 첫방문

        // d : 가로, 대각선
        if (d!=1) {
            if (c + 1 < N && map[r][c + 1] == 0) {
                dp[r][c][d] += pipe(r, c + 1, 0);
            }
        }
        // d : 세로, 대각선
        if (d!=0) {
            if (r+1 < N && map[r+1][c]==0) {
                dp[r][c][d] += pipe(r+1, c, 1);
            }
        }
        // 모든 경우
        if (r+1 < N && c+1 < N && map[r][c+1]+map[r+1][c]+map[r+1][c+1]==0) {
            dp[r][c][d] += pipe(r+1, c+1, 2);
        }

        return dp[r][c][d];
    }
}
