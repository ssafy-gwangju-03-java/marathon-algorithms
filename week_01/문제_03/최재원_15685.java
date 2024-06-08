import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 최재원_15685 {

    static int[] dr = {0, -1, 0, 1};
    static int[] dc = {1, 0, -1, 0};
    static boolean[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        arr = new boolean[101][101];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());

            dragon(x,y,d,g);
        }

        int answer = countSquare();

        System.out.println(answer);
        br.close();
    }

    private static int countSquare() {
        int answer = 0;

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if(arr[i][j] && arr[i+1][j] && arr[i][j+1] && arr[i+1][j+1])
                    answer += 1;
            }
        }

        return answer;
    }

    private static void dragon(int c, int r, int d, int g) {
        List<Integer> directions = new ArrayList<>();
        directions.add(d);

        for (int i = 0; i < g; i++) {
            for (int j = directions.size() - 1; j >= 0; j--) {
                directions.add((directions.get(j) + 1) % 4);
            }
        }

        arr[r][c] = true;

        for (int i = 0; i < directions.size(); i++) {
            r += dr[directions.get(i)];
            c += dc[directions.get(i)];
            arr[r][c] = true;
        }
    }
}
