import java.util.*;
import java.io.*;
public class 김가람_2636 {

    static int[][] grid;
    static int R;
    static int C;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] info = br.readLine().split(" ");
        R = Integer.parseInt(info[0]);
        C = Integer.parseInt(info[1]);

        grid = new int[R][C];
        for (int i = 0; i < R; i++) {
            String[] gridInfo = br.readLine().split(" ");
            for (int j = 0; j < C; j++) {
                grid[i][j] = Integer.parseInt(gridInfo[j]);
            }
        }

        int melted = 0;
        int time = 0;

        while (true) {
            int checkedCheeseCount = bfs();

            // 더 이상 녹일 치즈가 없으면 종료
            if (checkedCheeseCount == 0) {
                System.out.println(time);
                System.out.println(melted);
                break;
            }

            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (grid[i][j] == 2) {
                        grid[i][j] = 0;
                    }
                }
            }

            melted = checkedCheeseCount;
            time++;
        }
    }

    // 가장자리의 치즈를 2로 표시하고 그 수를 리턴해주는 BFS 함수
    public static int bfs() {
        boolean[][] visited = new boolean[R][C];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.addLast(new int[]{0, 0});
        visited[0][0] = true;
        int count = 0;

        while (!q.isEmpty()) {
            int[] curr = q.pollFirst();

            for (int d = 0; d < 4; d++) {
                int nr = curr[0] + dr[d];
                int nc = curr[1] + dc[d];

                if (0 <= nr && nr < R && 0 <= nc && nc < C && !visited[nr][nc]) {
                    visited[nr][nc] = true;

                    // 0이면 계속 탐색, 치즈를 만나면 2로 바꿔주기
                    if (grid[nr][nc] == 0) {
                        q.addLast(new int[]{nr, nc});
                    } else if (grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        count++;
                    }
                }
            }
        }

        return count;
    }
}