import java.io.*;
import java.util.*;

public class 정하림_5549 {
    static int N,M,K;
    static char[][] map;
    static int[][] jSum, oSum, iSum;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        map = new char[M + 1][];
        jSum = new int[M + 1][N + 1];
        oSum = new int[M + 1][N + 1];
        iSum = new int[M + 1][N + 1];

        for (int i = 1; i <= M; i++) {
            map[i] = br.readLine().toCharArray();
            for (int j = 1; j <= N; j++) {
                jSum[i][j] = jSum[i - 1][j] + jSum[i][j - 1] - jSum[i - 1][j - 1];
                oSum[i][j] = oSum[i - 1][j] + oSum[i][j - 1] - oSum[i - 1][j - 1];
                iSum[i][j] = iSum[i - 1][j] + iSum[i][j - 1] - iSum[i - 1][j - 1];

                if(map[i][j - 1] == 'J') jSum[i][j]++;
                else if(map[i][j - 1] == 'O') oSum[i][j]++;
                else iSum[i][j]++;
            }
        }

        StringBuilder ans = new StringBuilder();
        int a, b, c, d;
        int jResult, oResult, iResult;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());

            jResult = jSum[c][d] - jSum[c][b - 1] - jSum[a - 1][d] + jSum[a - 1][b - 1];
            oResult = oSum[c][d] - oSum[c][b - 1] - oSum[a - 1][d] + oSum[a - 1][b - 1];
            iResult = iSum[c][d] - iSum[c][b - 1] - iSum[a - 1][d] + iSum[a - 1][b - 1];
            ans.append(jResult + " " + oResult + " " + iResult + "\n");
        }

        System.out.println(ans);
    }
}