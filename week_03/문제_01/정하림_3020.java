import java.util.*;
public class 정하림_3020 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int H = sc.nextInt();

        int[] seok = new int[N/2];
        int[] jong = new int[N/2];
        for (int i = 0; i < N/2; i++) {
            seok[i] = sc.nextInt();
            jong[i] = sc.nextInt();
        }
        Arrays.sort(seok);
        Arrays.sort(jong);

        int minObs = N;
        int cnt = 0;
        for (int i = 1; i <= H; i++) {
            int low_seok = 0, high_seok = N / 2;
            int low_jong = 0, high_jong = N / 2;
            while (low_seok < high_seok) {
                int mid = (low_seok + high_seok) / 2;
                if (seok[mid] >= i) high_seok = mid;
                else low_seok = mid + 1;
            }
            while (low_jong < high_jong) {
                int mid = (low_jong + high_jong) / 2;
                if (jong[mid] >= H - i + 1) high_jong = mid;
                else low_jong = mid+1;
            }
            int obs = N - high_seok - high_jong;
            if (obs < minObs) {
                minObs = obs;
                cnt = 1;
            } else if (obs == minObs) {
                cnt++;
            }

        }

        System.out.print(minObs+" "+cnt);

    }
}

