import sys
from collections import deque

sys.stdin = open("../../input.txt")
input = sys.stdin.readline

N = int(input())
populations = list(map(int, input().split()))

# 인접 리스트 만들기
adjl = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0] + 1):
        adjl[i].append(arr[j])


# BFS로 한 덩이인지 확인
def bfs(subset):
    s = subset[0]
    q = deque()
    q.append(s)
    visited = [False] * (N + 1)
    visited[s] = True

    # 방문한 노드의 수 카운팅
    count = 1

    while q:
        curr = q.popleft()

        for next in adjl[curr]:
            # subset 내부에 있는 노드만 탐색
            if not visited[next] and next in subset:
                q.append(next)
                visited[next] = True
                count += 1

    return count


# subset이 모두 연결되어 있으면 True, 아니면 False
def is_connected(subset):
    count = bfs(subset)

    # 방문한 노드 수가 subset의 크기와 같으면 한덩이
    return count == len(subset)


min_v = 1000
districts = [i for i in range(1, N + 1)]

# 부분집합 만들기
for i in range(1 << N):
    subset1 = []
    subset2 = []
    for j in range(N):
        if i & (1 << j):
            subset1.append(districts[j])
        else:
            subset2.append(districts[j])

    # 두 부분집합이 모두 존재하고, 각각 연결되어 있으면
    if subset1 and subset2 and is_connected(subset1) and is_connected(subset2):
        # 각각의 합으로 최솟값 갱신하기
        sum1 = sum(populations[s - 1] for s in subset1)
        sum2 = sum(populations[s - 1] for s in subset2)

        min_v = min(min_v, abs(sum1 - sum2))

print(min_v if min_v != 1000 else -1)
