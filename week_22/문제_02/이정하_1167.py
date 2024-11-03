# 트리의 지름을 구하기
# 트리에서 임의의 정점 x에서 가장 먼 정점 y를 찾고, 
# 그 정점 y에서 가장 먼 정점 z를 찾으면 
# y와 z 사이의 거리가 트리의 지름이 됨
# 
# [해결 방법]
# 1. 스택을 이용한 DFS로 구현해서 재귀로 인한 메모리 사용을 줄임 메모리초과 그만나고싶다
# 2. 첫 번째 DFS: 임의의 정점(1번)에서 가장 먼 정점 찾기
# 3. 두 번째 DFS: 찾은 정점에서 가장 먼 정점까지의 거리 찾기
# 4. 입력을 sys로 처리해서 메모리 사용 최소화

import sys

input = sys.stdin.readline


def dfs(start):
    """
    스택을 이용한 반복적 DFS 구현
    start: 시작 노드
    returns: (가장 먼 노드, 그 노드까지의 거리)
    """
    # distance 배열 초기화 (-1은 방문하지 않은 상태를 표시)
    distance = [-1] * (v + 1)
    distance[start] = 0

    # 스택 초기화: (현재 노드, 현재까지의 거리)
    stack = [(start, 0)]
    max_dist = 0  # 최대 거리
    max_node = start  # 가장 먼 노드

    while stack:
        current, dist = stack.pop()

        # 현재 노드에서 연결된 모든 노드 확인
        for next_node, weight in tree[current]:
            # 방문하지 않은 노드라면
            if distance[next_node] == -1:
                next_dist = dist + weight
                distance[next_node] = next_dist
                stack.append((next_node, next_dist))

                # 최대 거리 갱신
                if next_dist > max_dist:
                    max_dist = next_dist
                    max_node = next_node

    return max_node, max_dist


# 노드 개수 v
v = int(input())

# 트리 정보를 저장할 인접 리스트 초기화
tree = [[] for _ in range(v + 1)]

# 트리 정보 입력 받기
for _ in range(v):
    # 입력을 정수 리스트로 변환
    data = list(map(int, input().split()))
    curr = data[0]  # 현재 노드 번호

    # 간선 정보 처리 (인덱스를 2씩 증가시키며 처리)
    i = 1
    while i < len(data):
        if data[i] == -1:  # 입력의 끝
            break
        # (연결된 노드, 가중치) 추가
        tree[curr].append((data[i], data[i + 1]))
        i += 2

# 첫 번째 DFS: 1번 노드에서 가장 먼 노드 찾기
far_node, _ = dfs(1)

# 두 번째 DFS: 가장 먼 노드에서 다시 가장 먼 노드 찾기
_, max_distance = dfs(far_node)

print(max_distance)