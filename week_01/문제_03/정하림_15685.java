package w1;

import java.util.*;

public class 정하림_15685 {

    static int[] dy = {0, -1, 0, 1};
    static int[] dx = {1, 0, -1, 0};
    static boolean[][] arr =new boolean[101][101];

    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int d = sc.nextInt();
            int g = sc.nextInt();
            dragonCurve(x, y, d, g);
        }

        int ans = 0;

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (arr[i][j] && arr[i + 1][j] && arr[i][j + 1] && arr[i + 1][j + 1]) {
                    ans += 1;
                }
            }
        }

        System.out.println(ans);
    }

    private static void dragonCurve(int x, int y, int d, int g) {
        List<Integer> D = new ArrayList<>();
        D.add(d);

        for (int i = 0; i < g; i++) {
            for (int j = D.size()-1; j >= 0; j--) {
                D.add((D.get(j) + 1) % 4);
            }
        }

        arr[y][x] = true;

        for (int i = 0; i < D.size(); i++) {
            y += dy[D.get(i)];
            x += dx[D.get(i)];
            arr[y][x] = true;
        }

    }
}
