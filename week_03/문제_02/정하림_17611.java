import java.util.*;

public class 정하림_17611 {
    static int n;
    static int[] xi, yi;
    static List<int[]> lineX = new ArrayList<>();
    static List<int[]> lineY = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        xi = new int[n];
        yi = new int[n];
        xi[0] = sc.nextInt();
        yi[0] = sc.nextInt();
        for (int i = 1; i < n; i++) {
            xi[i] = sc.nextInt();
            yi[i] = sc.nextInt();
            addLine(i, i-1);

        }
        addLine(0, n-1);

//        System.out.println(Math.max(Count(xi, lineX), Count(yi, lineY)));
        System.out.println(Math.max(Count(lineX), Count(lineY)));

    }

    private static void addLine(int i1, int i2) {
        if (xi[i1] == xi[i2]) {
            int[] tmp = yi[i1] < yi[i2] ? new int[]{yi[i1], yi[i2]} : new int[]{yi[i2], yi[i1]};
            lineY.add(tmp);
        } else {
            int[] tmp = xi[i1] < xi[i2] ? new int[]{xi[i1], xi[i2]} : new int[]{xi[i2], xi[i1]};
            lineX.add(tmp);
        }
    }
   // 스위핑 라인 알고리즘 //O(n log n)
      // 선분 교차, 겹치는 구간 찾기, 최근접 점 쌍 찾기 등의 문제
    private static int Count(List<int[]> lineX) {
        List<int[]> points = new ArrayList<>();
        for (int[] line : lineX) {
            points.add(new int[]{line[0], 1}); // 시작점
            points.add(new int[]{line[1], -1}); // 끝점
        }
        // 정렬 1. 시작점 먼저 2. 좌표
        points.sort((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);

        int max = 0, cnt = 0;
        for (int[] point : points) {
            cnt += point[1];
            max = Math.max(max, cnt);
        }
        return max;
    }

//    O(N^2)로 시간 초과
//    private static int Count(int[] xi, List<int[]> lineX) {
//        Arrays.sort(xi);
//        int maxV = -1;
//        for (int i = 0; i < n-1 ; i++) {
//            double V  = (double) (xi[i] + xi[i + 1]) /2;
//            int cnt = 0;
//            for (int[] x : lineX) {
//                if (x[0] < V && V < x[1]) {
////                    System.out.println(x[0]+"<"+ V +"<"+x[1]);
//                    cnt++;
//                }
//            }
//            maxV = Math.max(maxV, cnt);
//        }
//        return maxV;
//    }
}
