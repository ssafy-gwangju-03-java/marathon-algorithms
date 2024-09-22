import sys
from itertools import combinations
from collections import deque

n = int(sys.stdin.readline().rstrip())  # 구역 개수
people = list(map(int, sys.stdin.readline().rstrip().split()))  # 각 구역의 인구 수
arr = [[0 for _ in range(n)] for _ in range(n)]  # 인접행렬

for i in range(n):
    _, *dsts = map(int, sys.stdin.readline().rstrip().split())  # 각 구역 인접 정보
    for dst in dsts:
        arr[i][dst - 1] = 1  # 인접 행렬에 연결 정보 표시하기


def is_connected(nodes):
    q = deque()
    check = [False for _ in range(n)]  # 방문 여부 체크할 리스트
    q.append(nodes[0])  # 시작 노드 큐에 추가
    check[nodes[0]] = True  # 시작 노드 방문 체크

    while q:
        node = q.popleft()

        for i in range(len(arr[node])):
            if arr[node][i] == 0: continue  # 연결되지 않은 노드 건너뛰기
            if i not in nodes: continue  # 현재 선거구에 속하지 않은 노드 건너뛰기
            if not check[i]:
                check[i] = True  # 방문 표시하기
                q.append(i)  # 큐에 노드 추가하기

    return check.count(True) == len(nodes)  # 모든 노드 방문 여부 체크


def get_total(nodes):
    total = 0
    for node in nodes:
        total += people[node]  # 선거구의 총 인구 수 

    return total


cases = []
X = {i for i in range(n)}  # 전체 구역 집합
INF = int(1e9)
ans = INF

for i in range(1, n // 2 + 1):  # 가능한 모든 선거구 조합 생성하기
    As = tuple(combinations(X, i))  # i개의 구역으로 이루어진 모든 조합 생성하기
    for A in As:
        B = list(X.difference(A))  # B 선거구 생성하기

        if is_connected(A) and is_connected(B):  # 두 선거구가 모두 연결되어 있는지 확인하기
            a_total = get_total(A)  # A 선거구 총 인구 수 계산하기
            b_total = get_total(B)  # B선거구
            ans = min(ans, abs(a_total - b_total))  # 인구 차이 최솟값 갱신하기

if ans == INF:
    print(-1)  # 가능한 분할 없으면 -1 출력
else:
    print(ans)  # 인구 차이의 최솟값 출력하기
