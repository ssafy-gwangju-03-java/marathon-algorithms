from collections import deque


# 사이클에 속한 노드부터 BFS 탐색으로 나머지 노드의 거리를 구함
def BFS():
    que = deque()

    # 모든 노드들을 탐색하며 부모가 없는 노드(사이클에 속하는 노드)를 큐에 추가
    for i in range(N):
        if parents[i] == -1:
            # 사이클에 속한 노드의 거리는 0
            answer[i] = 0
            que.append(i)

    while que:
        current = que.popleft()

        # 현재 노드의 모든 자식 노드를 탐색
        for child in graph[current]:
            # 자식 노드의 거리가 아직 계산되지 않았다면
            if answer[child] == -1:
                # 현재 노드의 거리 + 1 을 자식 노드의 거리로 설정
                answer[child] = answer[current] + 1
                que.append(child)


# 노드N개
N = int(input())
# 구간 그래프 (인접 리스트)
graph = [[] for _ in range(N)]
# graph는 추후 BFS 탐색때 사용해야돼서, 노드 제거할 임시 그래프
temp = [[] for _ in range(N)]
# 각 노드의 간선 수 저장
graph_size = [0] * N
# 각 노드의 부모 노드 저장
parents = [-1] * N
# 각 노드의 거리(정답) 저장
answer = [-1] * N

for _ in range(N):
    s1, s2 = map(int, input().split())
    # 노드 번호가 1부터 시작하니까 1 뺀 값 저장
    graph[s1 - 1].append(s2 - 1)
    temp[s1 - 1].append(s2 - 1)
    graph_size[s1 - 1] += 1
    graph[s2 - 1].append(s1 - 1)
    temp[s2 - 1].append(s1 - 1)
    graph_size[s2 - 1] += 1

# 전체 탐색 후 간선 수가 1인 노드가 발견되지 않을 때까지 반복
while True:
    flag = True
    for i in range(N):
        if graph_size[i] == 1:
            # 간선이 1개인 노드의 부모를 설정
            parent = temp[i].pop()
            parents[i] = parent
            # 부모 노드에서 현재 노드를 제거
            temp[parent].remove(i)
            # 현재 노드의 간선 수를 0으로 설정
            graph_size[i] = 0
            # 부모 노드의 간선 수를 1 감소
            graph_size[parent] -= 1
            flag = False

    # 더 이상 간선 수가 1인 노드가 없으면 종료
    if flag:
        break

BFS()

print(*answer)
