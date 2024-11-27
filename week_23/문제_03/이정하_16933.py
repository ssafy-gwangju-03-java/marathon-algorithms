from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    # N: 세로 크기, M: 가로 크기, K: 부술 수 있는 벽의 최대 개수
    N, M, K = map(int, input().split())

    # 1x1 크기의 미로인 경우 바로 1 반환
    if N == 1 and M == 1:
        return 1

    # 미로 정보 입력 받기 (0: 이동 가능, 1: 벽)
    arr = [input()[:-1] for _ in range(N)]

    # 상하좌우 이동을 위한 방향 벡터
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 각 위치까지 도달하기 위해 부순 벽의 최소 개수를 저장하는 배열
    # 초기값은 K+1로 설정 (도달할 수 없는 상태를 표시)
    crack_count = [[K + 1] * M for _ in range(N)]
    crack_count[0][0] = 0  # 시작 위치는 벽을 부수지 않음

    # BFS를 위한 큐 초기화: (x좌표, y좌표, 부순 벽의 개수)
    que = deque([(0, 0, 0)])

    # 도착점의 좌표 미리 계산
    N_, M_ = N - 1, M - 1

    # 이동 횟수 (시간)
    ans = 1

    while que:
        # 현재 시간에 처리해야 할 위치의 개수
        l = len(que)

        # 현재 시간에 있는 모든 위치에 대해 처리
        for _ in range(l):
            ox, oy, crack = que.popleft()  # 현재 위치와 부순 벽의 개수

            # 도착점에 도달한 경우
            if ox == N_ and oy == M_:
                return ans

            # 현재 위치가 최소 벽 부순 횟수인 경우에만 처리
            elif crack == crack_count[ox][oy]:
                # 상하좌우 이동 시도
                for dx, dy in d:
                    x = ox + dx
                    y = oy + dy
                    # 미로 범위 내에 있는지 확인
                    if 0 <= x < N and 0 <= y < M:
                        # 현재까지 부순 벽의 개수가 다음 위치의 최소값보다 작은 경우
                        if crack < crack_count[x][y]:
                            # 다음 칸이 빈칸(0)인 경우
                            if arr[x][y] == '0':
                                crack_count[x][y] = crack
                                que.append((x, y, crack))

                            # 다음 칸이 벽(1)인 경우
                            else:
                                # 이미 더 적은 벽을 부수고 도달한 경우는 스킵
                                if crack + 1 >= crack_count[x][y]:
                                    continue

                                # 낮인 경우(홀수 시간)에만 벽을 부술 수 있음
                                elif ans & 1:
                                    crack_count[x][y] = crack + 1
                                    que.append((x, y, crack + 1))

                                # 밤인 경우 제자리에서 대기
                                else:
                                    que.append((ox, oy, crack))

        ans += 1  # 시간 증가

    return -1  # 도착점에 도달할 수 없는 경우


if __name__ == '__main__':
    print(solve())