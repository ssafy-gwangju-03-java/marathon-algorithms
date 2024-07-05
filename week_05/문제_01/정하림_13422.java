import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class 정하림_13422 {
    static int T, N, M;
    static long K;
    static int[] money;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        for (int tc=0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            money = new int[N];
            money = Stream.of(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int sum = 0;
            for (int i = 0; i < M; i++) {
                sum += money[i];
            }

            int ans = sum < K ? 1 : 0;
            if ( N == M ) {
                System.out.println(ans);
                continue;
            }

            for (int i = 1; i < N; i++) {
                sum = sum - money[i-1] + money[(i+M-1)%N];
                if (sum < K) ans++;
            }
            System.out.println(ans);
        }
    }
}

