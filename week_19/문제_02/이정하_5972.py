# 1. 입력 - 노드 수, 간선 수, 그래프 정보
# 2. 다익스트라 구현
#    a. 시작 노드 설정
#    b. 최단 거리 테이블 초기화
#    c. 시작 노드에서 다음을 반복
#       - 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
#       - 해당 노드를 거쳐 다른 노드로 가는 비용 계산
#       - 최단 거리 테이블 갱신
# 3. 시작점(1번 노드)에서 끝점(N번 노드)까지의 최단 거리 계산

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 1e9  # 무한대 값 설정


# 2. 다익스트라 구현
def dijkstra(graph, n):
    hq = [(0, 1)]  # 2.a. 우선순위 큐 초기화: (거리, 노드) 형태로 시작점 추가
    distance = [INF] * (n + 1)  # 2.b. 최단 거리 테이블 초기화
    distance[1] = 0  # 2.b. 시작점의 거리는 0으로 설정

    while hq:  # 2.c. 시작 노드에서 다음을 반복
        dist, cur = heappop(hq)  # 2.c. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
        if dist > distance[cur]:
            continue  # 이미 처리된 노드라면 무시
        for weight, next_node in graph[cur]:  # 2.c. 해당 노드를 거쳐 다른 노드로 가는 비용 계산
            next_dist = dist + weight
            if next_dist < distance[next_node]:  # 2.c. 최단 거리 테이블 갱신
                distance[next_node] = next_dist
                heappush(hq, (next_dist, next_node))

    print(distance[n])  # 3, 4. 도착점(n번 노드)까지의 최단 거리 출력


# 1. 입력 받기
n, m = map(int, input().split())  # 노드의 개수 n, 간선의 개수 m
graph = [[] for _ in range(n + 1)]  # 그래프 정보를 저장할 리스트

# 1-1. 간선 정보 입력받아 그래프 구성
for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 노드, 도착 노드, 가중치
    graph[s].append((w, e))  # 양방향 그래프임!!!
    graph[e].append((w, s))

# 2, 3, 4. 다익스트라 알고리즘 수행
dijkstra(graph, n)
