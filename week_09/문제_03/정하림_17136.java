import java.io.*;
import java.util.*;

import static java.util.Arrays.stream;


public class 정하림_17136 {

    static int[][] map = new int[10][10];
    static int[] arr = new int[6];
    static int min = 26;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i=0;i<10;i++){
            map[i] = stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
        Arrays.fill(arr,5);
        arr[0]=0;

        dfs();

        System.out.println(min>25?-1:min);
    }

    private static void dfs() {

        int[] point = find();

        if(point[0] == -1 && point[1]==-1){
            int cnt = 25 - stream(arr).sum();
            min = Math.min(min, cnt);
            return;
        }

        int x = point[0];
        int y = point[1];


        for (int size = 5; size >= 1; size--) {
            if (arr[size] > 0 && canAttach(x, y, size)) {
                attach(x, y, size);
                dfs();
                attach(x, y, size);
            }
        }

    }

    private static int[] find() {

        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if(map[i][j]==1)
                    return new int[]{j,i};
            }
        }
        return new int[]{-1,-1};
    }

    private static void attach(int x, int y, int size) {
        for (int i = y; i < y + size; i++) {
            for (int j = x; j < x + size; j++) {
                map[i][j]*=-1;
            }
        }

        arr[size] += map[y][x];
    }

    private static boolean canAttach(int x, int y, int size) {
        for(int i=y;i<y+size;i++){
            for(int j=x;j<x+size;j++){
                if(!isRange(j,i) || map[i][j]!=1)
                    return false;
            }
        }
        return true;
    }

    private static boolean isRange(int x, int y) {
        return x>=0&&y>=0&&x<10&&y<10;
    }
}