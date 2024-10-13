from itertools import combinations
from collections import deque
import sys

graph = []
#델타배열
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 5*5 격자 모든 위치
positions = [(i, j) for i in range(5) for j in range(5)]
# 25 중 7명 선택한 모든 조합
combs = list(combinations(positions, 7))
answer = 0

# 입력
for _ in range(5):
    graph.append(list(sys.stdin.readline().strip()))

# 다솜파(S) 4명 이상 확인
def checkDaSom(givenComb):
    daSom = 0
    for x, y in givenComb:
        if graph[x][y] == 'S':
            daSom += 1
    return True if daSom >= 4 else False

# 7명이 서로 인접해 있는지 확인
def checkAdjacent(givenComb):
    #bfs 초기 세팅
    visit = [False] * 7
    q = deque()
    q.append(givenComb[0])
    visit[0] = True

    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if (nx, ny) in givenComb:
                nextIdx = givenComb.index((nx, ny))
                if not visit[nextIdx]:
                    q.append((nx, ny))
                    visit[nextIdx] = True

    return False if False in visit else True

# 모든 조합에 대해 검사
for comb in combs:
    if checkDaSom(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)
