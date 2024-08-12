n = int(input())
scv = list(map(int, input().split()))
scv+=[0,0] # 1,2개만 입력되는 경우 뒤에 0으로 해야함
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)] # 최대 60이하이므로 61범위로 dp 테이블 생성
dp[scv[0]][scv[1]][scv[2]] = 0
lst = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]] # 모든 케이스 검사
for x in range(scv[0], -1, -1):
    for y in range(scv[1], -1, -1):
        for z in range(scv[2], -1, -1):
            if dp[x][y][z]==-1:
                continue
            for case in lst:
                nx = max(0, x - case[0])
                ny = max(0, y - case[1])
                nz = max(0, z - case[2])
                if (dp[nx][ny][nz] == -1 or dp[nx][ny][nz] > dp[x][y][z] + 1):  
                    # 아직 방문 x or 더 적은 횟수로 갱신(중간 과정에서는 필요없으나 (0,0,0)에서 갱신이 필요)
                    dp[nx][ny][nz] = dp[x][y][z] + 1
print(dp[0][0][0])