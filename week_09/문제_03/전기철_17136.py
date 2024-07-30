# 17136 색종이 붙이기

# 풀이 방식 - 위에서부터 쭉 돌면서 1 만날때마다 모든 붙일 수 있는 케이스 다 붙여보면서 확인
# if 3x3이 붙일 수 없으면 4x4 5x5도 불가능하므로 이부분 스킵을 통해 최적화 가능
# 백트래킹

lst = [list(map(int, input().split())) for _ in range(10)]
paper = [5, 5, 5, 5, 5]
ans = 26


# 종이 붙이기 -> 가능하면 True, 안되면 False
def post(y, x, width):
    for i in range(y, y + width + 1):
        for j in range(x, x + width + 1):
            if not lst[i][j]:
                return False
    return True


def play(y, x, cnt):
    global ans
    # 1. 오른쪽 끝까지 간 경우 (x==10) -> (0,y+1)칸 이동해서 다시 시작
    if x == 10:
        play(y + 1, 0, cnt)
        return
    # 2. 맨 밑까지 탐색이 끝난 경우 (y==10) -> ans 갱신
    if y == 10:
        ans = min(ans, cnt)
        return
    # 3. 1을 만나는 경우(붙일 수 있음) -> 1부터 5까지 다 붙여보면서 테스트
    if lst[y][x]:
        for i in range(5):
            if not paper[i]:  # 종이 없으면 넘어가기
                continue
            if y + i >= 10 or x + i >= 10:  # 칸 넘어가면 못붙임
                continue
            if not post(y, x, i):  # 지금 크기로 못붙임 -> 크기를 더 키울 이유가 없음
                break

            # 다 처리했으면 이제 붙이는 과정 진행
            for r in range(y, y + i + 1):
                for c in range(x, x + i + 1):
                    lst[r][c] = 0
            paper[i] -= 1

            play(y, x + 1, cnt + 1)

            # 원 상태로 복귀
            for r in range(y, y + i + 1):
                for c in range(x, x + i + 1):
                    lst[r][c] = 1
            paper[i] += 1
    # 4. 종이 못붙이는경우 (0) -> 다음칸
    else:
        play(y, x + 1, cnt)


play(0, 0, 0)

if ans == 26:
    print(-1)
else:
    print(ans)
