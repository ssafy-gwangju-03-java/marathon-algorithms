import sys

sys.stdin = open("../../input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))
arr = [[0] * M for _ in range(N)]


def staking_blocks(c):
    num = heights[c]
    for r in range(num):
        arr[N - r - 1][c] = 1


for i in range(M):
    staking_blocks(i)


# 왼쪽 어딘가와 오른쪽 어딘가에 블럭이 있으면 고일 수 있음
def can_pooled(r, c):
    for i in range(c - 1, -1, -1):  # 왼쪽에 블럭이 있는지 확인 + 없으면 False
        if arr[r][i] == 1:
            break
    else:
        return False

    for i in range(c + 1, M):  # 오른쪽에 블럭이 있는지 확인 + 없으면 False
        if arr[r][i] == 1:
            break
    else:
        return False

    return True  # 왼쪽과 오른쪽 모두 블럭이 있으면 True


# 빗물 수 세기
answer = 0
for r in range(N):  # 모든 칸 탐색
    for c in range(M):
        if arr[r][c] == 0 and can_pooled(r, c):  # 빈칸이고 빗물이 고일 수 있으면 + 1
            answer += 1

print(answer)
