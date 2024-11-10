import java.io.*;
import java.util.*;

class Node {
    int r, c, dist, broke, day;

    Node(int r, int c, int dist, int broke, int day) {
        this.r = r;
        this.c = c;
        this.dist = dist;
        this.broke = broke;
        this.day = day;
    }
}

public class 김가람_16933 {
    static final int dr[] = {0, 0, 1, -1};
    static final int dc[] = {1, -1, 0, 0};
    static int map[][];
    static boolean visit[][][][];
    static int N, M, K, ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        K = Integer.parseInt(input[2]);
        map = new int[N][M];
        visit = new boolean[N][M][K + 1][2];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j) - '0';
            }
        }

        ans = -1;
        bfs();
        System.out.println(ans);
    }

    static void bfs() {
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0, 0, 1, 0, 0));
        visit[0][0][0][0] = true;

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int r = curr.r;
            int c = curr.c;

            if (r == N - 1 && c == M - 1) {
                ans = curr.dist;
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (0 > nr || nr >= N || 0 > nc || nc >= M) continue;

                // 이동할 곳이 벽이 아닌 경우
                if (map[nr][nc] == 0) {
                    // 낮에 이동하는 경우 (day가 0)
                    if (curr.day == 0 && !visit[nr][nc][curr.broke][1]) {
                        visit[nr][nc][curr.broke][1] = true;
                        q.add(new Node(nr, nc, curr.dist + 1, curr.broke, 1));
                    }
                    // 밤에 이동하는 경우 (day가 1)
                    else if (curr.day == 1 && !visit[nr][nc][curr.broke][0]) {
                        visit[nr][nc][curr.broke][0] = true;
                        q.add(new Node(nr, nc, curr.dist + 1, curr.broke, 0));
                    }
                }
                // 벽인 경우
                else {
                    // 벽을 부순 횟수가 K 미만인 경우 벽을 부술 수 있음
                    if (curr.broke < K) {
                        // 낮에 벽을 부수는 경우
                        if (curr.day == 0 && !visit[nr][nc][curr.broke + 1][1]) {
                            visit[nr][nc][curr.broke + 1][1] = true;
                            q.add(new Node(nr, nc, curr.dist + 1, curr.broke + 1, 1));
                        }
                        // 밤에 벽을 부수는 경우
                        else if (curr.day == 1 && !visit[r][c][curr.broke][0]) {
                            visit[r][c][curr.broke][0] = true;
                            q.add(new Node(r, c, curr.dist + 1, curr.broke, 0));
                        }
                    }
                }
            }
        }
    }
}