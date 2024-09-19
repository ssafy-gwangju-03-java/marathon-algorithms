import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class 김가람_23309 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int M = Integer.parseInt(firstLine[1]);

        int[] stations = new int[N];

        // 고유 번호가 i인 역의 이전 역, 다음 역 == prev[i], next[i]
        int[] prev = new int[1_000_001];
        int[] next = new int[1_000_001];

        String[] stationInput = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            stations[i] = Integer.parseInt(stationInput[i]);
        }

        for (int i = 0; i < N; i++) {
            int curr = stations[i];
            prev[curr] = stations[(i - 1 + N) % N];
            next[curr] = stations[(i + 1) % N];
        }

        StringBuilder ans = new StringBuilder();

        for (int k = 0; k < M; k++) {
            String[] command = br.readLine().split(" ");

            if (command[0].equals("BN")) {
                int i = Integer.parseInt(command[1]);
                int j = Integer.parseInt(command[2]);

                int nextNode = next[i];
                prev[j] = i;
                next[j] = nextNode;
                next[i] = j;
                prev[nextNode] = j;

                ans.append(nextNode).append("\n");

            } else if (command[0].equals("BP")) {
                int i = Integer.parseInt(command[1]);
                int j = Integer.parseInt(command[2]);

                int prevNode = prev[i];
                prev[j] = prevNode;
                next[j] = i;
                next[prevNode] = j;
                prev[i] = j;

                ans.append(prevNode).append("\n");

            } else if (command[0].equals("CN")) {
                int i = Integer.parseInt(command[1]);

                int toDelete = next[i];
                int nextNext = next[toDelete];
                next[i] = nextNext;
                prev[nextNext] = i;

                ans.append(toDelete).append("\n");

            } else if (command[0].equals("CP")) {
                int i = Integer.parseInt(command[1]);

                int toDelete = prev[i];
                int prevPrev = prev[toDelete];
                next[prevPrev] = i;
                prev[i] = prevPrev;

                ans.append(toDelete).append("\n");
            }
        }

        System.out.print(ans.toString());
    }
}