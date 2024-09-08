# 계란으로 계란치기

def dfs(n, cnt):
    global ans

    # 가지치기 조건 추가할 수도(무조건 좋은 건 x, 비교하면서 시간 더 걸릴 수도)
    # 끝까지 진행해도 정답 갱신 불가한 경우
    # if ans >= (cnt + (N-n) * 2):
    #     return

    # 모든 계란을 손에 들고 부딪치기 완료
    if n == N:
        ans = max(ans, cnt)
        return
    # 현재 계란이 깨진 경우 -> 다음 계란으로
    if arr[n][0] <= 0:
        dfs(n+1, cnt)
    # 현재 계란 안깨진 경우
    else:
        # 한번도 안 부딪혔다면 다음 계란으로
        flag = False
        # 하나씩 부딪쳐보기
        for j in range(N):
            if n ==j or arr[j][0] <= 0:
                continue
            flag = True
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n+1, cnt + int(arr[n][0] <= 0) + int(arr[j][0] <= 0))
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]
        if flag == False:
            dfs(n+1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# 계란 index, 깨진 계란 개수
dfs(0, 0)
print(ans)

# 참고
# https://www.youtube.com/watch?v=QgG1hIkrZME [문어박사 IT 편의점]