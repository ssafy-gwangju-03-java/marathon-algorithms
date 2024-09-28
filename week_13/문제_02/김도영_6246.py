import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 방문해야 할 m개의 노드
node = []
for _ in range(m):
    x, y = map(int, input().split())
    node.append([x - 1, y - 1])

# 방향 벡터
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

result = 0
start_i, start_j = node[0]
visited = [[0] * n for _ in range(n)]
visited[start_i][start_j] = 1

def dfs(i, j, visited, idx):
    global result

    # 현재 방문한 노드가 마지막 노드라면 경로를 하나 찾은 것이므로 result 증가
    if idx == m - 1:
        result += 1
        return

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        # 인덱스 검사 & 방문 체크
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            # 벽이 아닐 때
            if board[ni][nj] != 1:
                visited[ni][nj] = 1
                # 다음 방문해야 할 노드일 경우에만 이동
                if ni == node[idx + 1][0] and nj == node[idx + 1][1]:
                    dfs(ni, nj, visited, idx + 1)
                
                else:
                    dfs(ni, nj, visited, idx)
                
                visited[ni][nj] = 0

dfs(start_i, start_j, visited, 0)

print(result)