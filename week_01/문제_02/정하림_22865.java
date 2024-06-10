package w1;

import java.util.*;

public class 정하림_22865 {
    static int N, A, B, C, M;
    static List<List<int[]>> graph = new ArrayList<>();
    static long[] length; // 자바 푸는 사람 롱 쓰자........
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        length = new long[N+1];
        Arrays.fill(length, Long.MAX_VALUE);

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();

        M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            int D = sc.nextInt();
            int E = sc.nextInt();
            int L = sc.nextInt();
            graph.get(D).add(new int[]{E, L});
            graph.get(E).add(new int[]{D, L});
        }

        dijkstra(A);
        dijkstra(B);
        dijkstra(C);
//        System.out.println(Arrays.toString(length));

        long max = -1;
        int ans = -1;
        for (int i = 1; i <= N; i++) {
            //
            if (i == A && i == B && i == C) continue;

            if (length[i] > max) {
                max = length[i];
                ans = i;
            }
        }
        System.out.println(ans);
    }
    private static void dijkstra(int start){
        long[] tmpLength = new long[N+1];
        Arrays.fill(tmpLength, Long.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e[1]));
        pq.offer(new int[]{start, 0});
        tmpLength[start] = 0;
        while (!pq.isEmpty()){
            int[] poll = pq.poll();
            int nowI = poll[0];
            int nowL = poll[1];
            if (tmpLength[nowI] < nowL) {
                continue;
            }
            for (int[] nxt : graph.get(nowI)) {
                int nxtI = nxt[0];
                int newL = nowL + nxt[1];

                if (tmpLength[nxtI] > newL) {
                    tmpLength[nxtI] = newL;
                    pq.offer(new int[]{nxtI, newL});
                }
            }
        }
//        System.out.println(Arrays.toString(tmpLength));
        for (int i = 1; i <= N; i++) {
            if (length[i] > tmpLength[i]) {
                length[i] = tmpLength[i];
            }
        }
    }
}
