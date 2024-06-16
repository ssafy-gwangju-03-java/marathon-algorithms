import java.util.Scanner;

public class 정하림_2600 {
    static int[] beads;
    static int K1, K2;
    static char ans = 'B';
    static boolean[][] dp = new boolean[501][501];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        beads = new int[]{sc.nextInt(), sc.nextInt(), sc.nextInt()};
        for (int tc = 0; tc < 5; tc++) {
            K1 = sc.nextInt();
            K2 = sc.nextInt();
            game(K1, K2);
            if (dp[K1][K2]) {
                System.out.println("A");
            } else {
                System.out.println("B");
            }
        }
    }

    private static void game(int K1, int K2) {
        if (dp[K1][K2]) return;

        for (int k1 = 0; k1 <= K1; k1++) {
            for (int k2 = 0; k2 <= K2; k2++) {
                for (int b : beads) {
                    boolean caseK1 = k1 >= b && !dp[k1 - b][k2];
                    boolean caseK2 = k2 >= b && !dp[k1][k2 - b];
                    if (caseK1|| caseK2) {
                        dp[k1][k2] = true;
                        break;
                    }
                }
            }
        }
    }


}
