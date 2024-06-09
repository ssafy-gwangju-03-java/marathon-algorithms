import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 최재원_22865 {
    static int N, M;
    static int A, B, C;
    static ArrayList<Node>[] list;

    static class Node implements Comparable<Node> {
        int to;
        int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        list = new ArrayList[N + 1];

        for (int i = 1; i < N + 1; i++) {
            list[i] = new ArrayList<>();
        }

        st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            list[from].add(new Node(to, cost));
            list[to].add(new Node(from, cost));
        }

        long[] dist1 = dijkstra(A);
        long[] dist2 = dijkstra(B);
        long[] dist3 = dijkstra(C);

        int answer = selectNode(dist1, dist2, dist3);


        System.out.println(answer);
        br.close();
    }

    private static int selectNode(long[] dist1, long[] dist2, long[] dist3) {
        int answer = 0;
        long compareDistance = 0;

        for (int i = 1; i <= N; i++) {
            long minDistance = Math.min(dist1[i], Math.min(dist2[i], dist3[i]));

            // 거리가 같으면 건너뛰기 -> 작은번호 선택
            if (minDistance == compareDistance) {
                continue;
            }

            //거리가 멀면 선택
            if (minDistance > compareDistance) {
                compareDistance = minDistance;
                answer = i;
            }
        }

        return answer;
    }

    private static long[] dijkstra(int start) {
        long[] dist = new long[N + 1];

        for (int i = 1; i <= N; i++) {
            dist[i] = Long.MAX_VALUE;
        }

        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();

        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node currentNode = pq.poll();

            int cur = currentNode.to;
            int distance = currentNode.cost;

            if (dist[cur] < distance) {
                continue;
            }

            for (int i = 0; i < list[cur].size(); i++) {

                int nxt_distance = distance + list[cur].get(i).cost;
                int nxt = list[cur].get(i).to;

                if (dist[nxt] > nxt_distance) {
                    dist[nxt] = nxt_distance;
                    pq.add(new Node(nxt, nxt_distance));
                }
            }
        }

        return dist;
    }
}
