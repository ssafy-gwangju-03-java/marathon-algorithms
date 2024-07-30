import sys

input = sys.stdin.readline # 입력 데이터가 많아서 그냥 input하면 시간초과
m, n = map(int, input().split())
k = int(input())
lst = [list(map(str, input())) for _ in range(m)]

jmap = [[0] * (n + 1) for _ in range(m + 1)] # (1,1)부터 정글 누적합 저장할 리스트
imap = [[0] * (n + 1) for _ in range(m + 1)]
omap = [[0] * (n + 1) for _ in range(m + 1)]

for y in range(m):
    for x in range(n):
        jmap[y + 1][x + 1] = jmap[y + 1][x] + jmap[y][x + 1] - jmap[y][x] # ex) (2,2)합은 (1,2)까지 누적합+ (2,1)까지 누적합 - (1,1) 누적합(2번 더해졌으므로)
        imap[y + 1][x + 1] = imap[y + 1][x] + imap[y][x + 1] - imap[y][x]
        omap[y + 1][x + 1] = omap[y + 1][x] + omap[y][x + 1] - omap[y][x]

        if lst[y][x] == "J": # 마지막에 리스트값 확인해서 추가해주기
            jmap[y + 1][x + 1] += 1
        elif lst[y][x] == "I":
            imap[y + 1][x + 1] += 1
        else:
            omap[y + 1][x + 1] += 1
for _ in range(k):
    a, b, c, d = map(int, input().split())
    ans_j = jmap[c][d] - jmap[a - 1][d] - jmap[c][b - 1] + jmap[a - 1][b - 1] # 조사 영역 누적합 구하기
    ans_i = imap[c][d] - imap[a - 1][d] - imap[c][b - 1] + imap[a - 1][b - 1]
    ans_o = omap[c][d] - omap[a - 1][d] - omap[c][b - 1] + omap[a - 1][b - 1]

    print(ans_j, ans_o, ans_i)
