import java.util.*;
import java.io.*;

public class 김가람_21609 {
    static int N;
    static int M;
    static int[][] grid;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] constants = br.readLine().split(" ");
        N = Integer.parseInt(constants[0]);
        M = Integer.parseInt(constants[1]);

        grid = new int[N][N];

        for (int i = 0; i < N; i++) {
            String[] nums = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(nums[j]);
            }
        }

        int score = 0;

        // 오토 플레이
        while (true) {
            visited = new boolean[N][N];
            boolean hasBlockGroup = false;
            PriorityQueue<BlockGroup> blockGroups = new PriorityQueue<>();

            // 모든 블록 그룹 찾기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j]) {
                        BlockGroup currBlockGroup = bfs(i, j);
                        if (currBlockGroup != null){
                            hasBlockGroup = true;
                            blockGroups.add(currBlockGroup);
                        }
                    }
                }
            }

            // 블록 그룹이 없으면 게임 종료
            if (!hasBlockGroup) break;

            // 크기가 가장 큰 블록그룹
            BlockGroup chosenGroup = blockGroups.poll();
            score += (int) Math.pow(chosenGroup.numOfBlock, 2);

            // 선택된 블록 그룹 제거 (빈 칸 -2로 표시)
            for (int[] loc : chosenGroup.coords) {
                int r = loc[0];
                int c = loc[1];
                grid[r][c] = -2;
            }

            // 중력 적용과 회전 단계 수행
            fall();
            rotate();
            fall();
        }

        System.out.println(score);

    }

    // 중력 적용
    static void fall() {
        for (int c = 0; c < N; c++) {
            int idx = N - 1;
            for (int r = N - 1; r >= 0; r--) {
                if (grid[r][c] >= 0) {
                    grid[idx][c] = grid[r][c];
                    if (idx != r) grid[r][c] = -2;
                    idx--;
                } else if (grid[r][c] == -1) {
                    idx = r - 1;
                }
            }
        }
    }

    // 반시계 방향으로 회전
    static void rotate() {
        int[][] rotatedArray = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                rotatedArray[N - 1 - j][i] = grid[i][j];
            }
        }

        grid = rotatedArray;
    }

    static BlockGroup bfs(int r, int c) {
        // 무지개 블록은 방문처리하지 않고 탐색도 하지 않음
        // 무지개 블록은 다른 블록 탐색할 때 중복으로 탐색되어야 하므로
        if (grid[r][c] == 0) return null;

        visited[r][c] = true;

        // 검은 블록이면 방문처리만 하고 탐색은 하지 않음
        if (grid[r][c] < 0) return null;

        // 탐색해야 할 블록 그룹의 색
        int originVal = grid[r][c];

        // BFS에 사용할 큐
        Deque<int[]> q = new ArrayDeque<>();

        // 일반 블록을 넣어줄 우선순위 큐 (기준 블록을 쉽게 구하기 위함)
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (o1, o2) -> {
                    if (o1[0] != o2[0]) return o1[0] - o2[0];
                    else return o1[1] - o2[1];
                }
        );

        // 무지개 블록을 넣어줄 배열
        ArrayList<int[]> rainbow = new ArrayList<>();

        q.add(new int[]{r, c});

        while (!q.isEmpty()) {
            int[] curr = q.pollFirst();
            int currVal = grid[curr[0]][curr[1]];

            // 일반 블록과 무지개 블록을 구분해서 넣어준다
            if (currVal == 0) {
                rainbow.add(new int[]{curr[0], curr[1]});
            } else if (currVal == originVal) {
                pq.add(new int[]{curr[0], curr[1]});
            }

            for (int d = 0; d < 4; d++) {
                int nr = curr[0] + dr[d];
                int nc = curr[1] + dc[d];
                if (0 <= nr && nr < N && 0 <= nc && nc < N && !visited[nr][nc] && (grid[nr][nc] == 0 || grid[nr][nc] == originVal)) {
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc});
                }
            }
        }

        // 그룹에는 일반 블록이 적어도 하나 있어야 하며 그룹에 속한 블록의 개수는 2보다 크거나 같아야 한다
        if (pq.size() > 0 && (pq.size() + rainbow.size() > 1)) {

            // BlockGroup을 생성하기 위해 필요한 값들
            int numOfBlock = pq.size() + rainbow.size();
            int numOfRainbow = rainbow.size();
            int[] base = pq.peek();
            int baseR = base[0];
            int baseC = base[1];
            ArrayList<int[]> coords = new ArrayList<>();
            coords.addAll(pq);
            coords.addAll(rainbow);

            // 무지개 블록의 방문처리를 되돌려준다 (다른 색 블록들을 탐색할 때 또 필요하므로)
            for (int[] ints : rainbow) {
                visited[ints[0]][ints[1]] = false;
            }

            BlockGroup blockGroup = new BlockGroup(numOfBlock, numOfRainbow, baseR ,baseC, coords);
            return blockGroup;
        }

        // 블록 그룹이 형성될 조건에 부합하지 않으면 null 리턴
        return null;
    }

    static class BlockGroup implements Comparable<BlockGroup> {
        int numOfBlock;
        int numOfRainbow;
        int baseR;
        int baseC;
        ArrayList<int[]> coords;

        BlockGroup(int numOfBlock, int numOfRainbow, int baseR, int baseC, ArrayList<int[]> coords) {
            this.numOfBlock = numOfBlock;
            this.numOfRainbow = numOfRainbow;
            this.baseR = baseR;
            this.baseC = baseC;
            this.coords = coords;
        }

        // 우선순위 비교 (블록 수, 무지개 블록 수, 행, 열 순)
        @Override
        public int compareTo(BlockGroup o) {
            if (this.numOfBlock != o.numOfBlock) {
                return (this.numOfBlock - o.numOfBlock) * -1;
            } else {
                if (this.numOfRainbow != o.numOfRainbow) {
                    return (this.numOfRainbow - o.numOfRainbow) * -1;
                } else {
                    if (this.baseR != o.baseR) {
                        return (this.baseR - o.baseR) * -1;
                    } else {
                        return (this.baseC - o.baseC) * -1;
                    }
                }
            }
        }
    }
}