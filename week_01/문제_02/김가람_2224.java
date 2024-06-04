import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 김가람_2224 {
    static int N;
    static boolean[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        // A, B, C, ... x, y, z (52개)
        // 전건과 후건의 사이의 참거짓 여부를 표시해 줄 행렬
        graph = new boolean[52][52];

        // 입력
        for (int i = 0; i < N; i++) {
            String statement = br.readLine();
            char[] node = new char[]{statement.charAt(0), statement.charAt(5)};

            // 전건 == 후건이면 continue
            if (node[0] == node[1]) continue;

            int[] indices = new int[2];

            for (int j = 0; j < 2; j++) {
                char c = node[j];
                if (Character.isUpperCase(c)) {
                    indices[j] = c - 65;
                } else {
                    indices[j] = c - 97 + 26;
                }
            }

            graph[indices[0]][indices[1]] = true;
        }

        // 플로이드 워셜
        // k 위치 잘못 설정해서 오답
        // - k는 항상 반복문의 가장 바깥에 위치해야 함
        // - k가 만약 반복문의 가장 안쪽에 있다면 i, j의 연결 여부는 그저 단순하고 순차적으로 갱신될 뿐임
        // 참고 : https://github.com/ssafy-gwangju-03-java/ssafy-gwangju3-java-algorithms/blob/master/week_09_%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC/%EA%B9%80%EA%B0%80%EB%9E%8C/B_1_14938.java
        for (int k = 0; k < 52; k++) {
            for (int i = 0; i < 52; i++) {
                for (int j = 0; j < 52; j++) {
                    if (graph[i][j] || i == j) continue;
                    graph[i][j] = (graph[i][k] && graph[k][j]);
                }
            }
        }


        // 명제로 변환해 담아줄 배열
        ArrayList<char[]> statements = new ArrayList<>();

        // 현재 인덱스로 표현된 전건, 후건을 다시 Char로 변경
        // 52가 아닌 58로 잡았다면 거치치 않아도 되었을 과정 ('Z'와 'a'의 아스키값 차이는 6밖에 안됨...)
        for (int i = 0; i < 52; i++) {
            for (int j = 0; j < 52; j++) {
                if (graph[i][j]) {
                    int[] indices = new int[]{i, j};
                    char[] chars = new char[2];

                    for (int k = 0; k < 2; k++) {
                        if (indices[k] < 26) {
                            chars[k] = (char) (indices[k] + 65);
                        } else {
                            chars[k] = (char) (indices[k] - 26 + 97);
                        }
                    }

                    statements.add(chars);
                }
            }
        }

        statements.sort((o1, o2) -> (o1[0] != o2[0]) ? o1[0] - o2[0] : o1[1] - o2[1]);

        System.out.println(statements.size());

        for (char[] statement : statements) {
            System.out.println(statement[0] + " => " + statement[1]);
        }
    }
}
