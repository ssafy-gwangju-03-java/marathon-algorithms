import java.util.*;

public class 정하림_14466 {
    static int N, K, R;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] bridge, cow, map;
    static int cnt;
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();
        R = sc.nextInt();

        bridge = new int[R][4];
        for (int i = 0; i < R; i++) {
            bridge[i] = new int[]{sc.nextInt() - 1, sc.nextInt() - 1,
                                  sc.nextInt() - 1, sc.nextInt() - 1};
        }
        cow = new int[K][2];
        for (int i = 0; i < K; i++) {
            cow[i] = new int[]{sc.nextInt() - 1, sc.nextInt() - 1};
        }
        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(map[i], -1);
        }

        for (int i = 0; i < K; i++) {
            if (map[cow[i][0]][cow[i][1]] == -1) {
                bfs(cow[i], i);
            }

        }
        int cnt = 0;
        for(int i =0 ; i < K-1 ; i++){
            for(int j = i+1 ; j < K ; j++){
                if(map[cow[i][0]][cow[i][1]] != map[cow[j][0]][cow[j][1]]) {
                    cnt ++;
                }
            }
        }

        System.out.println(cnt);

    }

    private static void bfs(int[] cow, int idx) {
        boolean[][] visited = new boolean[N][N];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{cow[0], cow[1]});
        visited[cow[0]][cow[1]] = true;
        map[cow[0]][cow[1]] = idx;
        while(!q.isEmpty()){
            int r = q.peek()[0];
            int c = q.poll()[1];
            for(int d = 0 ; d < 4 ; d++){
                int nr = r+dr[d];
                int nc = c+dc[d];
                if (0 <= nr && nr < N && 0 <= nc && nc < N && !visited[nr][nc]) {
                    boolean flag = true;
                    for (int[] b : bridge) {
                        if (b[0] == r && b[1] == c && b[2] == nr && b[3] == nc) {
                            flag = false;
                            break;
                        }
                        if (b[2] == r && b[3] == c && b[0] == nr && b[1] == nc) {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) {
                        q.offer(new int[]{nr, nc});
                        visited[nr][nc] = true;
                        map[nr][nc] = idx;
                    }

                }
            }
        }
    }
}
