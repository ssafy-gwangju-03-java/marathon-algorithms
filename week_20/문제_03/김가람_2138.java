import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 김가람_2138 {
    static int N;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        boolean[] bulbList = new boolean[N];
        boolean[] targetList = new boolean[N];

        String bulbString = br.readLine();
        String targetString = br.readLine();

        for (int i = 0; i < N; i++) {
            if (bulbString.charAt(i) == '1') {
                bulbList[i] = true;
            }
        }

        for (int i = 0; i < N; i++) {
            if (targetString.charAt(i) == '1') {
                targetList[i] = true;
            }
        }

        // didPressFirst : 0번 전구가 이미 눌렸는지 아닌지에 대한 경우의 수를 판별함
        int result1 = switchBulb(bulbList, targetList, false);
        int result2 = switchBulb(bulbList, targetList, true);

        System.out.println((result1 != -1 && result2 != -1) ? Math.min(result1, result2) : Math.max(result1, result2));
    }

    private static int switchBulb(boolean[] bulbList, boolean[] targetList, boolean didPressFirst) {
        int count = 0;
        boolean[] copiedBulbList = Arrays.copyOf(bulbList, N);

        if (didPressFirst) {
            copiedBulbList[0] = !copiedBulbList[0];
            copiedBulbList[1] = !copiedBulbList[1];
            count++;
        }

        // i번 전구가 목표치인 targetList의 i번 전구와 다르면 그 다음 전구의 스위치를 누른다
        for (int i = 1; i < N; i++) {
            if (copiedBulbList[i - 1] != targetList[i - 1]) {
                copiedBulbList[i - 1] = !copiedBulbList[i - 1];
                copiedBulbList[i] = !copiedBulbList[i];
                if (i < N - 1) copiedBulbList[i + 1] = !copiedBulbList[i + 1];
                count++;
            }
        }

        // greedy 탐색을 완료한 전구가 목표치와 같으면 스위치를 누른 횟수를 반환
        return Arrays.equals(copiedBulbList, targetList) ? count : -1;
    }
}