import sys
from collections import deque
sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

# N:층수, K:디스플레이 자리수, P:반전시킬 LED 수, X:멈춰있는 층
N, K, P, X = map(int, input().split())

# 숫자별 켜져있는 LED
seven_segments = [
    '1110111',
    '0010010',
    '1011101',
    '1011011',
    '0111010',
    '1101011',
    '1101111',
    '1010010',
    '1111111',
    '1111011'
]

# required_led[r][c]  r이 c 되기 위해 반전시켜야 할 LED 수
required_led = [[0] * 10 for _ in range(10)]


for r in range(10):
    for c in range(10):
        cnt = 0
        if r != c:
            for i in range(7):
                if seven_segments[r][i] != seven_segments[c][i]:
                    cnt += 1
        required_led[r][c] = cnt

answer = 0

def dfs(idx, subsum, X, made):
    global answer

    # 지금까지 반전시킨 LED 수가 P를 초과하면 백트래킹
    if subsum > P:
        return

    # 전부 바꿨으면
    if idx == K:
        # 뽑힌 숫자 합치기
        lst = list(made)

        total = 0
        for i in range(len(made)):
            total += lst.pop() * (10 ** i)

        # 만들어진 층수가 최대 층수 이하이거나 0이 아니면 정답 + 1
        if total <= N and total != 0:
            answer += 1

        return

    # 일의자리 숫자 뽑기
    target = X % 10

    # 숫자를 모든 숫자로 바꿔보기
    for i in range(10):
        made.appendleft(i)
        dfs(idx + 1, subsum + required_led[target][i], X // 10, made)
        made.popleft()

made = deque()

dfs(0, 0, X, made)

# 하나도 바꾸지 않은 경우 1개 제외
print(answer - 1)

