import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 정하림_6987 {
    static int maxCnt = 6;
    static int[][] game;
    static boolean endFlag = false;
    static String ans = "";
    static int[][] worldCup;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int size = 0;
        for(int i = 1; i < maxCnt; i++) {
            size += i;
        }

        game = new int[size][2];
        int idx = 0;
        for(int i = 0; i < maxCnt - 1; i++) {
            for(int j = i + 1; j < maxCnt; j++) {
                game[idx][0] = i;
                game[idx][1] = j;
                idx++;
            }
        }

        for (int tc = 0; tc < 4; tc++) {
            st = new StringTokenizer(br.readLine());
            worldCup = new int[3][maxCnt];
            boolean isPossible = true;

            for(int i = 0; i < maxCnt; i++) {
                int win = Integer.parseInt(st.nextToken());
                int draw = Integer.parseInt(st.nextToken());
                int lose = Integer.parseInt(st.nextToken());

                worldCup[0][i] = win;
                worldCup[1][i] = draw;
                worldCup[2][i] = lose;

                if(win + draw + lose != 5) {
                    isPossible = false;
                    break;
                }
            }

            if(isPossible) {
                backTracking(worldCup, 0, size);
                ans += endFlag ? "1" : "0";
            }
            else ans += "0";

            ans += " ";
            endFlag = false;
        }

        System.out.print(ans);
    }

    private static void backTracking(int[][] worldCup, int cnt, int size) {
        if(endFlag) return;


        if(cnt == size) {
            endFlag = true;
            return;
        }

        int me = game[cnt][0];
        int opp = game[cnt][1];

        // 승 to 패
        if(worldCup[0][me] > 0 && worldCup[2][opp] > 0) {
            worldCup[0][me]--;
            worldCup[2][opp]--;
            backTracking(worldCup, cnt + 1, size);
            worldCup[0][me]++;
            worldCup[2][opp]++;
        }
        // 무 to 무
        if(worldCup[1][me] > 0 && worldCup[1][opp] > 0) {
            worldCup[1][me]--;
            worldCup[1][opp]--;
            backTracking(worldCup, cnt + 1, size);
            worldCup[1][me]++;
            worldCup[1][opp]++;
        }
        // 패 to 승
        if(worldCup[2][me] > 0 && worldCup[0][opp] > 0) {
            worldCup[2][me]--;
            worldCup[0][opp]--;
            backTracking(worldCup, cnt + 1, size);
            worldCup[2][me]++;
            worldCup[0][opp]++;
        }
    }


}