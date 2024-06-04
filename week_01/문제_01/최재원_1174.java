import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 최재원_1174 {
    static int N;
    static int[] nums = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

    static List<Long> arr = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        subset(0, 0);
        Collections.sort(arr);

        System.out.println(N > arr.size() - 1 ? -1 : arr.get(N));
    }

    private static void subset(int idx, long num) {
        if (idx == nums.length) {
            arr.add(num);
            return;
        }

        subset(idx + 1, num * 10 + nums[idx]);
        subset(idx + 1, num);
    }
}
