# https://www.acmicpc.net/problem/2224

## Referenced
# https://velog.io/@kimdukbae/플로이드-워셜-알고리즘-Floyd-Warshall-Algorithm
# https://www.acmicpc.net/board/view/86647

import sys

input = sys.stdin.readline

# ord('A') = 65 -> ord('Z') = 90
# ord('a') = 97 -> ord('z') = 122
# 총 52개, 중간 포함 58개

N = int(input())
INF = int(1e9)  # 미연결 간선의 가중치
adjm = [[INF] * 58 for _ in range(58)]

# 자기 자신은 언제나 도달 가능
for i in range(58):
    for j in range(58):
        if i == j:
            adjm[i][j] = 0

for i in range(N):
    thesis = list(input().rstrip())
    idx_r = ord(thesis[0]) - 65
    idx_c = ord(thesis[-1]) - 65
    # P => P 입력 예외 설정
    if idx_r != idx_c:
        adjm[idx_r][idx_c] = 1

# 플로이드-워셜 이용
# 명제 간 간선 설정 후 다른 명제들을 통해 증명할 수 있는 모든 명제 탐색
# 모든 노드를 경유하는 경우를 탐색
for k in range(58):
    # 출발 노드
    for a in range(58):
        # 도착 노드
        for b in range(58):
            # 기존의 간선의 가중치와 k 노드를 경유하는 경우 중 최소치를 인접행렬에 저장
            # 이 문제에선 경유지로 도달 가능한 간선의 연결 유무만 필요하기 때문에 최소치의 의미는 없음
            adjm[a][b] = min(adjm[a][b], adjm[a][k] + adjm[k][b])

count = 0
pre_condition, post_condition = [], []  # 전건, 후건
for r in range(58):
    for c in range(58):
        # 경유지를 포함하여 간선이 연결되어 있을 경우 증명 가능한 명제
        if 0 < adjm[r][c] < INF:
            count += 1
            pre_condition.append(chr(r + 65))
            post_condition.append(chr(c + 65))

print(count)
for i in range(len(pre_condition)):
    print(pre_condition[i], "=>", post_condition[i])
