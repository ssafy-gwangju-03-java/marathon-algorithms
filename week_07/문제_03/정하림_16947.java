import java.util.*;

public class 정하림_16947 {
    static int N;
    static int[] dis;
    static boolean[] visited;
    static boolean isCycle;
    static List<Integer>[] adj;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        visited = new boolean[N];
        dis = new int[N];
        Arrays.fill(dis, -1);

        adj = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            adj[a].add(b);
            adj[b].add(a);
        }

        DFS(-1, 0);
        BFS();

        for (int d : dis) {
            System.out.print(d + " ");
        }
        System.out.println();
    }

    private static void BFS() {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            if (dis[i] == 0) q.add(i);
        }

        int cnt = 1;
        while (!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                int poll = q.poll();
                for (int a : adj[poll]) {
                    if (dis[a] != -1) continue;
                    dis[a] = cnt;
                    q.add(a);
                }
            }
            cnt++;
        }
    }

    private static void DFS(int prev, int now) {
        visited[now] = true;
        for (int nxt : adj[now]) {
            if (visited[nxt] && nxt != prev) {
                isCycle = true;
                dis[nxt] = 0;
                break;
            } else if (!visited[nxt]) {
                DFS(now, nxt);
                if (isCycle) {
                    if (dis[nxt] == 0) isCycle = false;
                    else dis[nxt] = 0;
                    return;
                }
            }
        }
    }
}