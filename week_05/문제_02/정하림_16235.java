import java.util.*;
import java.lang.*;
import java.io.*;

public class 정하림_16235 {
    static int N, M, K;
    static int[][] map, A;
    static PriorityQueue<int[]> tree;
    static int[] dr = {-1,-1,-1,0,0,1,1,1};
    static int[] dc = {-1,0,1,-1,1,-1,0,1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        K = sc.nextInt();

        map = new int[N][N];
        A = new int[N][N];
        for (int i=0; i < N; i++) {
            for (int j=0; j < N; j++) {
                map[i][j] = 5;
                A[i][j] = sc.nextInt();
            }
        }

        tree = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        for (int i=0; i < M; i++) {
            int r = sc.nextInt()-1;
            int c = sc.nextInt()-1;
            int age = sc.nextInt();
            tree.add(new int[]{age, r, c});
        }
        for (int k = 0; k < K; k++) {
            if (SS()) {
                System.out.println(0);
                return;
            }
//            System.out.println(k+"년 "+tree.size());
        }
        System.out.println(tree.size());


    }
    private static boolean SS() {
        PriorityQueue<int[]> tmp = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        List<int[]> mapTmp = new ArrayList<>();
        while (!tree.isEmpty()) {
            int[] poll = tree.poll();
//            System.out.println("봄이다 "+Arrays.toString(poll));
            int age = poll[0];
            int r = poll[1];
            int c = poll[2];
            if (map[r][c] >= age) {
                tmp.add(new int[]{age+1, r, c});
                map[r][c] -= age;
            } else {
                mapTmp.add(new int[] {age/2, r, c});
            }
        }
        if (tmp.size() == 0) {
            return true;
        }
        tree = new PriorityQueue<>(tmp);
        for (int i=0; i < mapTmp.size(); i++) {
            int[] add = mapTmp.get(i);
            map[add[1]][add[2]] += add[0];
        }
        F(tmp);
        return false;
    }
    private static void F(PriorityQueue<int[]> tmp) {
        while (!tmp.isEmpty()) {
            int[] poll = tmp.poll();
            int age = poll[0];
            int r = poll[1];
            int c = poll[2];
            if (age % 5 == 0) {
                for (int d = 0; d < 8; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                        tree.add(new int[] {1, nr, nc});
                    }
                }
            }
        }
        W();

    }
    private static void W() {
        for (int i= 0; i < N; i++) {
            for (int j =0; j < N; j++){
                map[i][j] += A[i][j];
            }
        }
    }
}