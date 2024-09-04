# 16987 계란으로 계란치기

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def dfs(idx):  # 맨 왼쪽부터 시작 / 끝까지 가면 개수 세서 갱신
    global ans
    # print(lst,idx)
    if idx == n:  # 끝까지 가면
        cnt = 0
        for i in range(n):
            if lst[i][0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return
    if lst[idx][0] <= 0:
        dfs(idx + 1)
    else:
        chk = 1  # 깰 달걀 있나 확인
        for i in range(n):
            if i != idx and lst[i][0] > 0:
                chk = 0  # 타겟 달걀 있음
                lst[i][0] -= lst[idx][1]
                lst[idx][0] -= lst[i][1]
                dfs(idx + 1)
                lst[i][0] += lst[idx][1]
                lst[idx][0] += lst[i][1]
        if chk:  # 나머지 달걀이 다 깨져서 깰게 없음 -> 끝으로
            dfs(n)


dfs(0)
print(ans)
