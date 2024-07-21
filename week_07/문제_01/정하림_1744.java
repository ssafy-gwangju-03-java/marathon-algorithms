import java.util.*;

public class 정하림_1744 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n == 1) {
            System.out.println(sc.nextInt());
            return;
        }

        List<Integer> pos = new ArrayList<>(); // 양수
        List<Integer> neg = new ArrayList<>(); // 음수

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            if (num > 0) pos.add(num);
            else neg.add(num);
        }

        Collections.sort(neg);
        Collections.sort(pos, Collections.reverseOrder());

        int total = 0;
        while (neg.size() > 1) {
            total += neg.get(0) * neg.get(1);
            neg.remove(0);
            neg.remove(0);
        }

        while (pos.size() > 1) {
            int p1 = pos.get(0);
            int p2 = pos.get(1);

            if (p1 + p2 > p1 * p2) {
                total += p1;
                pos.remove(0);
            } else {
                total += p1 * p2;
                pos.remove(0);
                pos.remove(0);
            }
        }

        if (!neg.isEmpty() && neg.get(0) != 0) {
            total += neg.remove(0);
        }

        if (!pos.isEmpty()) {
            total += pos.remove(0);
        }

        System.out.println(total);
    }
}