# 1. 가장 큰 그룹을 찾기 (BFS)
# 2. 그룹 제거 후 중력 적용
# 3. 맵 회전 후 다시 중력 적용
# 4. 더 이상 제거할 그룹이 없을 때까지 반복

from collections import deque

# n: 맵의 크기, m: 색상의 개수
n, m = map(int, input().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 맵 정보 입력 받기
for i in range(n):
    graph.append(list(map(int, input().split())))


def find_group(a, b):
    """
    (a, b)에서 시작해서 같은 색상의 블록 그룹을 찾는 함수
    BFS로 인접한 같은 색상 블록들 탐색
    """
    visited = [[False] * n for _ in range(n)]  # 방문 체크 배열
    groupQ = []  # 현재 그룹에 속한 블록들의 좌표를 저장할 리스트

    # 빈 공간이거나 이미 제거된 블록인 경우 종료
    if graph[a][b] == -1 or graph[a][b] == -2:
        return

    # 시작 블록의 색상 저장 (0은 무지개 블록)
    myColor = graph[a][b] if graph[a][b] > 0 else 0
    cnt = 1  # 그룹에 속한 블록 수

    # BFS 시작
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        groupQ.append((x, y))

        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵 범위 체크 및 방문 여부 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            # 벽이거나 제거된 블록 체크
            if graph[nx][ny] == -1 or graph[nx][ny] == -2:
                continue
            # 색상 체크 (무지개 블록이나 같은 색상만 가능)
            if graph[nx][ny] > 0:
                if myColor == 0:
                    myColor = graph[nx][ny]
                elif myColor != graph[nx][ny]:
                    continue
            cnt += 1
            queue.append((nx, ny))
            visited[nx][ny] = True

    # 그룹 크기가 2 미만이면 무시
    if cnt < 2:
        return

    global groupCnt, maxQ

    # 현재 그룹이 기존 최대 그룹보다 큰 경우
    if cnt > groupCnt:
        groupCnt = cnt
        maxQ = groupQ
    # 크기가 같은 경우 우선순위 비교
    elif cnt == groupCnt:
        # 무지개 블록 수 계산
        thisZeroCnt, maxZeroCnt = 0, 0
        for i in range(cnt):
            if graph[groupQ[i][0]][groupQ[i][1]] == 0:
                thisZeroCnt += 1
        for i in range(groupCnt):
            if graph[maxQ[i][0]][maxQ[i][1]] == 0:
                maxZeroCnt += 1

        # 무지개 블록 수가 같은 경우
        if thisZeroCnt == maxZeroCnt:
            # 행과 열 기준으로 정렬하여 기준 블록 찾기
            groupQ.sort(key=lambda x: x[1])
            groupQ.sort(key=lambda x: x[0])
            maxQ.sort(key=lambda x: x[1])
            maxQ.sort(key=lambda x: x[0])
            gx, gy, mx, my = 0, 0, 0, 0
            # 일반 블록 중 기준 블록 찾기
            for i in range(cnt):
                if graph[groupQ[i][0]][groupQ[i][1]] != 0:
                    gx, gy = groupQ[i][0], groupQ[i][1]
                    break
            for i in range(groupCnt):
                if graph[maxQ[i][0]][maxQ[i][1]] != 0:
                    mx, my = maxQ[i][0], maxQ[i][1]
                    break

            # 기준 블록 위치 비교
            if gx > mx:
                maxQ = groupQ
            elif gx == mx:
                if gy > my:
                    maxQ = groupQ
        # 무지개 블록 수가 더 많은 경우
        elif thisZeroCnt > maxZeroCnt:
            maxQ = groupQ
    return


def gravity():
    """
    중력을 적용하는 함수
    아래에서부터 위로 검사하며 빈 공간이 있으면 블록을 아래로 이동
    """
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if graph[i][j] != -1:  # 벽이 아닌 경우
                tmp = i
                # 아래로 이동 가능한 만큼 이동
                while tmp + 1 < n and graph[tmp + 1][j] == -2:
                    graph[tmp + 1][j] = graph[tmp][j]
                    graph[tmp][j] = -2
                    tmp += 1


def rotate():
    """
    맵을 반시계 방향으로 90도 회전하는 함수
    """
    newGraph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newGraph[n - 1 - j][i] = graph[i][j]
    return newGraph


# 메인 게임 로직
answer = 0  # 점수 합계

while True:
    groupCnt = 0  # 현재 가장 큰 그룹의 크기
    maxQ = []  # 현재 가장 큰 그룹의 블록 좌표들

    # 모든 위치에서 그룹 찾기 시도
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:  # 일반 블록에서만 시작
                find_group(i, j)

    # 더 이상 제거할 그룹이 없으면 종료
    if not maxQ:
        break

    # 점수 추가 (그룹 크기의 제곱)
    answer += len(maxQ) ** 2

    # 선택된 그룹 제거
    for x, y in maxQ:
        graph[x][y] = -2

    # 중력 적용
    gravity()
    # 회전
    graph = rotate()
    # 다시 중력 적용
    gravity()

print(answer)