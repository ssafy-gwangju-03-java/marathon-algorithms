import java.io.*;
import java.util.*;
import java.lang.*;

public class 정하림_1600 {
    static int K, N, M;
    static int[][] board;
    static boolean[][][] visited;
    static int[] dr = {-2, -2, 2, 2, -1, -1, 1, 1, -1, 1, 0, 0};
    static int[] dc = {-1, 1, -1, 1, -2, 2, -2, 2, 0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        board = new int[N][M];
        visited = new boolean[N][M][K+1];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(bfs());
    }
    private static int bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 0, K});
        visited[0][0][K] = true;
        while (!q.isEmpty()) {
            int[] poll = q.poll();
//            System.out.println(Arrays.toString(poll));
            int r = poll[0];
            int c = poll[1];
            int cnt =  poll[2];
            int k = poll[3];

            if (r == N - 1 && c == M - 1) return cnt;

            if (k > 0) {
                for (int d = 0; d < 8; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (0 <= nr && nr < N && 0 <= nc && nc < M && !visited[nr][nc][k-1] && board[nr][nc] != 1) {
                        visited[nr][nc][k-1] = true;
                        q.add(new int[]{nr, nc, cnt+1, k-1});
                    }
                }
            }
            for (int d = 8; d < 12; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (0 <= nr && nr < N && 0 <= nc && nc < M && !visited[nr][nc][k] && board[nr][nc] != 1) {
                    visited[nr][nc][k] = true;
                    q.add(new int[]{nr, nc, cnt+1, k});
                }
            }
        }
        return -1;
    }
}
