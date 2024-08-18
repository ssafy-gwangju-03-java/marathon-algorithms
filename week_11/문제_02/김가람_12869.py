import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
SCV = list(map(int, sys.stdin.readline().split()))
for _ in range(3 - N):
    SCV.append(0)

attack =[(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 3, 9), (1, 9, 3)]
memo = {}

def dfs(p, q, r):

    # 종료조건: 모든 SCV의 체력이 소진
    if (p, q, r) == (0, 0, 0):
        return 0

    # 이미 계산된 결과가 있다면 가져옴
    if (p, q, r) in memo:
        return memo[(p, q, r)]

    min_attack = 100

    for i in range(6):
        min_attack = min(dfs(
            max(p - attack[i][0], 0),
            max(q - attack[i][1], 0),
            max(r - attack[i][2], 0)
        ) + 1, min_attack)

    memo[(p, q, r)] = min_attack
    return min_attack

print(dfs(*SCV))