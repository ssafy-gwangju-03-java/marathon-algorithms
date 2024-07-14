    import java.util.*;
    import java.io.*;

    public class 정하림_2146{
        static int N;
        static int ans = 10001;
        static int[][] map = new int[101][101];
        static boolean[][] isIsland = new boolean[101][101];
        static int[] dr = {0,1,0,-1};
        static int[] dc = {1,0,-1,0};

        public static void main(String[] args) throws Exception{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;

            N = Integer.parseInt(br.readLine());

            for(int i=0;i<N;i++){
                st = new StringTokenizer(br.readLine());
                for(int j=0;j<N;j++){
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int cnt = 1;
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    if(!isIsland[i][j] && map[i][j] != 0){
                        dfs(i,j,cnt);
                        cnt++;
                    }
                }
            }

            for(int i=1;i<=cnt;i++){
                int[][] map_copied = map.clone();
                bfs(map_copied,i);
            }

            System.out.println(ans);
        }

        private static void dfs(int r, int c, int cnt){
            isIsland[r][c] = true;
            map[r][c] = cnt;

            for(int d=0;d<4;d++){
                int nr = r + dr[d];
                int nc = c + dc[d];
                if(nr<0 || nr>=N || nc<0 || nc>=N) continue;

                if(map[nr][nc] != 0 && !isIsland[nr][nc]) dfs(nr,nc,cnt);
            }
        }

        private static void bfs(int[][] map, int cnt){
            boolean[][] visited = new boolean[101][101];
            Queue<int[]> queue = new LinkedList<>();

            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    if(map[i][j] == cnt){
                        queue.add(new int[]{i,j,0});
                        visited[i][j] = true;
                    }
                }
            }

            while(!queue.isEmpty()){
                int[] poll = queue.poll();

                for(int i=0;i<4;i++){
                    int nr = poll[0] + dr[i];
                    int nc = poll[1] + dc[i];
                    if(nr<0 || nr>=N || nc<0 || nc>=N) continue;

                    if(map[nr][nc] != cnt && map[nr][nc] != 0){
                        if(ans > poll[2] && poll[2] != 0) ans = poll[2];
                    }
                    else{
                        if(map[nr][nc]==0 && !visited[nr][nc]){
                            visited[nr][nc] = true;
                            queue.add(new int[]{nr,nc, poll[2]+1});
                        }
                    }
                }
            }
        }
    }
