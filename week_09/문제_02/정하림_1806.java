import java.io.*;
import java.util.*;

public class 정하림_1806 {
    static int N, S;
    static int[] arr;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        arr = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());


        int start = 0;
        int end = 0;
        int len = Integer.MAX_VALUE;
        int sum = 0;
        while (start <= end && end <= N) {
            if (sum < S) {
                sum += arr[end++];
            } else {
                len = Math.min(len, end - start);
                sum -= arr[start++];
            }
        }
        if (len == Integer.MAX_VALUE) {
            System.out.println(0);
        } else System.out.println(len);
    }
}