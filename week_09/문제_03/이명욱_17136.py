def color(x, y, N, cnt):
    # 가장 작은 경우의 수 저장
    global n_min
    # 색종이의 1을 전부 가릴수 있는지 판별
    global now
    if N == 0:
        if n_min > cnt:
            n_min = cnt
            now = True
            return
    # x방향 범위를 벗어나면 다음 칸으로 이동
    if x >= 10:
        color(0, y+1, N, cnt)
        return
    # y방향 범위를 벗어나면 함수 종료
    if y >= 10:
        return
    if lst[y][x]:
        # 5칸짜리 색종이부터 1칸짜리까지 실행
        for n in range(4, -1, -1):
            # n+1칸짜리 색종이의 갯수가 5개가 아니라면
            if paper[n] < 5:
                # 붙인 색종이가 10x10의 범위안에 있다면
                if x+n < 10 and y+n < 10:
                    num = True
                    for i in range(n+1):
                        for j in range(n+1):
                            # (n+1)x(n+1) 색종이를 붙일 수 있는지 판단
                            if not lst[y+i][x+j]:
                                num = False
                    # (n+1)x(n+1) 색종이를 붙일 수 있다면
                    if num:
                        for i in range(n+1):
                            for j in range(n+1):
                                lst[y+i][x+j] = 0
                        a = (n+1)**2
                        N -= a
                        cnt += 1
                        paper[n] += 1
                        # 색종이를 붙이고 다음 경우의 수를 실행
                        color(x+n+1, y, N, cnt)
                        # 색종이를 붙이지 않고 다음 경우의 수를 실행
                        for i in range(n+1):
                            for j in range(n+1):
                                lst[y+i][x+j] = 1
                        N += a
                        cnt -= 1
                        paper[n] -= 1
    # 종이 위에 칸이 1이 아니라면 다음 칸으로 이동
    else:
        color(x+1, y, N, cnt)

lst = [list(map(int,input().split())) for _ in range(10)]
paper = [0] * 5
n_min = 26
N = 0
now = False
for i in lst:
    N += i.count(1)
color(0, 0, N, 0)
if now:
    print(n_min)
else:
    print(-1)