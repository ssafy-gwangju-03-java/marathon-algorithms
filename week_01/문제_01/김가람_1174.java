import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 김가람_1174 {
    static int N;
    static long ans = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dfs(1, 0);
        System.out.println(ans);
    }

    static void dfs(int lev, long num) {
        // 가장 큰 줄어드는 수 == 9876543210
        if (num > 9876543210L) {
            return;
        }

        long offer = num;                               // num 대신 연산에 사용할 카피본
        int digit = Long.toString(num).length() - 1;    // 현재 숫자의 자릿수
        boolean decreasing = true;                      // 줄어드는 수인지 체크해줄 bool 값

        // 가장 큰 자릿수부터 줄여가며 체크
        while (offer > 0) {
            int currDigit = (int) (offer / Math.pow(10, digit));
            offer %= (int) Math.pow(10, digit);
            int nextDigit = (int) (offer / Math.pow(10, digit - 1));
            if (nextDigit >= currDigit) {
                decreasing = false;
                break;
            }
            digit--;
        }

        // 100과 같이 뒤의 숫자가 두개 이상의 0으로 이루어진 경우 위의 while문 자릿수 체크에 걸리지 않고 빠져나오므로 한번 더 걸러줌
        // 나눌 수 있는 데까지 나눴는데 digit이 남아있다 == 체크 미완료
        if (digit > 0) {
            decreasing = false;
        }

        if (decreasing) {
            if (lev == N) {
                ans = num;
            } else {
                dfs(lev + 1, num + 1);
            }
        } else {
            // 211 -> 220, 220 -> 300로 건너뛰기
            num /= (long) Math.pow(10, digit);
            num++;
            num *= (long) Math.pow(10, digit);
            dfs(lev, num);
        }
    }
}
