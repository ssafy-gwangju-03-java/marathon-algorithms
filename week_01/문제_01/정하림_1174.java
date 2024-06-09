package w1;

import java.util.*;

public class 정하림_1174 {
    static List<Long> list = new ArrayList<>();
    static int n;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n = sc.nextInt();

        if(n >= Math.pow(2,10)) {
            System.out.println(-1);
        }
        else {
            dfs(0,9);
            Collections.sort(list);
//                System.out.println(list.toString());
            System.out.println(list.get(n-1));
        }
    }

    private static void dfs(long sum, int num) {
        if(!list.contains(sum)) {
            list.add(sum);
        }
        if(num < 0) return;

        dfs(sum * 10 + num, num - 1);
        dfs(sum, num - 1);
    }
}