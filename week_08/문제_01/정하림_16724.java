import java.io.*;
import java.util.*;

public class 정하림_16724 {

    static int N, M, cnt;
    static char[][] map;
    static boolean[][] visited;
    static boolean[][] finished;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static char[] move = {'U', 'D', 'L', 'R'};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new char[N][M];
        visited = new boolean[N][M];
        finished = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j]) {
                    dfs(i, j);
                }
            }
        }
        System.out.println(cnt);
    }

    public static void dfs(int r, int c) {
        visited[r][c] = true;

        for (int d = 0; d < 4; d++) {
            if (map[r][c] == move[d]) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nr >= N || nc < 0 || nc >= M) break;
                if (!visited[nr][nc]) {
                    dfs(nr, nc);
                }
                else {
                    if (!finished[nr][nc]) cnt++;
                }
                break;
            }
        }
        finished[r][c] = true;
    }
}
