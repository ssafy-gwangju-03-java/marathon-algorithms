import java.util.*;
import java.io.*;

public class 김가람_1167 {
    static int N;
    static ArrayList<ArrayList<int[]>> adjl;

    public static void main(String[] args) throws IOException {

        /*
        * 참조: https://blogshine.tistory.com/111
        * 트리의 지름 알고리즘
        * */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        adjl = new ArrayList<>(N + 1);

        for (int i = 0; i < N + 1; i++) {
            adjl.add(new ArrayList<>());
        }

        for (int i = 1; i < N + 1; i++) {
            String[] ipt = br.readLine().split(" ");
            int curr = Integer.parseInt(ipt[0]);

            for (int j = 1; j < ipt.length - 1; j += 2) {
                int next = Integer.parseInt(ipt[j]);
                int dist = Integer.parseInt(ipt[j + 1]);

                adjl.get(curr).add(new int[]{next, dist});
            }
        }

        // 임의의 노드(여기서는 첫번째)로 부터 가장 먼 정점을 구한다
        int[] furthestFromFirst = bfs(1);

        // 가장 먼 정점으로부터 다시 가장 먼 정점을 구한다
        int[] furthestFromFurthest = bfs(furthestFromFirst[0]);

        System.out.println(furthestFromFurthest[1]);
    }

    // new int[]{가장 먼 정점 번호, 거리}를 리턴함
    static int[] bfs(int startNode) {
        boolean[] visited = new boolean[N + 1];

        Deque<int[]> q = new ArrayDeque<>();

        q.add(new int[]{startNode, 0});
        visited[startNode] = true;

        int maxDist = -1;
        int furthestNode = startNode;

        while (!q.isEmpty()) {
            int[] currVal = q.pollFirst();
            int currNode = currVal[0];
            int currDist = currVal[1];

            if (currDist > maxDist) {
                maxDist = currDist;
                furthestNode = currNode;
            }

            for (int[] nodeInfos : adjl.get(currNode)) {
                if (!visited[nodeInfos[0]]) {
                    int nextNode = nodeInfos[0];
                    int nextDist = nodeInfos[1];

                    visited[nextNode] = true;
                    q.add(new int[]{nextNode, currDist + nextDist});
                }
            }
        }

        return new int[]{furthestNode, maxDist};
    }
}