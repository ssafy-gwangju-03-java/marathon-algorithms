import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 김가람_15685 {
    static boolean[][] arr;
    static int[] dr = {0, -1, 0, 1};
    static int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        arr = new boolean[101][101];

        for (int i = 0; i < N; i++) {
            String[] info = br.readLine().split(" ");
            int r = Integer.parseInt(info[1]);
            int c = Integer.parseInt(info[0]);
            int d = Integer.parseInt(info[2]);
            int b = Integer.parseInt(info[3]);
            dragonCurve(r, c, d, b);
        }

        int ans = 0;

        // 정사각형 여부 체크
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (arr[i][j] && arr[i + 1][j] && arr[i][j + 1] && arr[i + 1][j + 1]) {
                    ans++;
                }
            }
        }

        System.out.println(ans);
    }

    static void dragonCurve(int r, int c, int d, int g) {
        ArrayList<Integer> dirs = new ArrayList<>();
        dirs.add(d);

        /*
        * 0세대: 0
        * 1세대: 0, 1
        * (0, 1) -> 뒤집기 (1, 0) -> ++1 -> (2, 1)
        * 2세대: (0, 1) + (2, 1)
        * (0, 1, 2, 1) -> 뒤집기 (1, 2, 1, 0) -> ++1 -> (2, 3, 2, 1)
        * 3세대: (0, 1, 2, 1) + (2, 3, 2, 1)
        * ...
        * 뒤집은 후 1씩 더해서 기존 방향에 더해주기
        * */

        while (g-- > 0) {
            for (int i = dirs.size() - 1; i >= 0; i--) {
                int dir = (dirs.get(i) + 1) % 4;
                dirs.add(dir);
            }
        }

        arr[r][c] = true;

        for (int n : dirs) {
            arr[r += dr[n]][c += dc[n]] = true;
        }

    }
}
