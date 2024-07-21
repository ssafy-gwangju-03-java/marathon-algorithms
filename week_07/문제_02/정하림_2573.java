import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class 정하림_2573 {
    static int N, M;
    static int[][] arr;
    static List<int[]> icebergs = new ArrayList<>();
    static int t = 0;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        t = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] != 0) icebergs.add(new int[]{arr[i][j], i, j});
            }
        }

        while (true) {
            t++;
            melt();

            int cnt = countGroups();

            if (cnt >= 2) {
                System.out.println(t);
                break;
            }

            if (icebergs.isEmpty()) {
                System.out.println(0);
                break;
            }
        }
    }

    private static void melt() {
        List<int[]> tmp = new ArrayList<>();
        for (int[] ice : icebergs) {
            int h = ice[0], r = ice[1], c = ice[2];
            int waterCnt = 0;
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < N && nc >= 0 && nc < M && arr[nr][nc] == 0) waterCnt++;
            }
            if (h - waterCnt > 0) {
                tmp.add(new int[]{h - waterCnt, r, c});
            }
        }

        icebergs = tmp;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = 0;
            }
        }
        for (int[] ice : icebergs) {
            arr[ice[1]][ice[2]] = ice[0];
        }
    }

    private static int countGroups() {
        boolean[][] visited = new boolean[N][M];
        int cnt = 0;
        for (int[] ice : icebergs) {
            int r = ice[1], c = ice[2];
            if (!visited[r][c]) {
                bfs(r, c, visited);
                cnt++;
            }
        }
        return cnt;
    }

    private static void bfs(int r, int c, boolean[][] visited) {
        Queue<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{r, c});
        visited[r][c] = true;

        while (!dq.isEmpty()) {
            int[] curr = dq.poll();
            int cr = curr[0];
            int cc = curr[1];

            for (int d = 0; d < 4; d++) {
                int nr = cr + dr[d];
                int nc = cc + dc[d];
                if (nr >= 0 && nr < N && nc >= 0 && nc < M && arr[nr][nc] != 0 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    dq.offer(new int[]{nr, nc});
                }
            }
        }
    }
}