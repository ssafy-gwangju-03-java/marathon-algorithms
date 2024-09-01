# https://softeer.ai/practice/6246

## Referenced
# https://papapapa.tistory.com/122
# https://www.youtube.com/watch?v=PAihI2CGr-M

import sys

sys.setrecursionlimit(100000)


def pathfinder(cur_pos, adjl, visited):
    if visited[cur_pos]:
        return

    # 방문하지 않은 노드 방문처리
    visited[cur_pos] = 1
    for node in adjl[cur_pos]:
        pathfinder(node, adjl, visited)


N, M = map(int, input().split())

# 단방향 그래프이지만 S와 T에서 출발하는 두 방향 모두 탐색해야하므로
# 인접리스트 (정/역방향) 2개 생성
adjl_s = [[] for _ in range(N)]
adjl_t = [[] for _ in range(N)]

# 출발지 S/T와 정/역방향 4개 방문 리스트 생성
visited_from_s = [0] * N
visited_from_t = [0] * N
visited_to_s = [0] * N
visited_to_t = [0] * N

for _ in range(M):
    s, t = map(int, input().split())
    adjl_s[s - 1].append(t - 1)
    adjl_t[t - 1].append(s - 1)

S, T = map(int, input().split())
S -= 1
T -= 1

visited_from_s[T] = 1
visited_from_t[S] = 1
pathfinder(S, adjl_s, visited_from_s)
pathfinder(T, adjl_s, visited_from_t)

pathfinder(S, adjl_t, visited_to_s)
pathfinder(T, adjl_t, visited_to_t)

# 모든 방문리스트에 공통적으로 방문한 노드 갯수 센 후 출/도착지 제외
result = 0
for i in range(N):
    if visited_from_s[i] and visited_from_t[i] and visited_to_s[i] and visited_to_t[i]:
        result += 1

print(result - 2)
