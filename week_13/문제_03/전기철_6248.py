# 6248 출퇴근길
import sys

sys.setrecursionlimit(10**6)


def dfs(now, lst, vis):
    if vis[now]:
        return
    vis[now] = 1
    for x in lst[now]:
        dfs(x, lst, vis)


input = sys.stdin.readline
n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
lstReverse = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    lstReverse[e].append(s)

s, t = map(int, input().split())

startS = [0] * (n + 1)
startS[t] = 1
dfs(s, lst, startS)
startT = [0] * (n + 1)
startT[s] = 1
dfs(t, lst, startT)
endS = [0] * (n + 1)
dfs(s, lstReverse, endS)
endT = [0] * (n + 1)
dfs(t, lstReverse, endT)

# startS = [0] * (n + 1)
# startT = [0] * (n + 1)
# endS = [0] * (n + 1)
# endT = [0] * (n + 1)
# startS[t] = 1
# startT[s] = 1

# dfs(s, lst, startS)
# dfs(t, lst, startT)
# dfs(s, lstReverse, endS)
# dfs(t, lstReverse, endT)
# 이렇게 몰아놓고 하니까 메모리초과나서 하나씩 했는데 통과 -> 이유는 모르겠다 이건

# idea : 정방향 역방향 그래프를 모두 이용해서 모두 해당되는 부분 -> 왕복 가능한 영역이라는 점을 이용

cnt = 0
for i in range(1, n + 1):
    if startS[i] and startT[i] and endS[i] and endT[i]:  # 다 해당되면 cnt+=1
        cnt += 1
        # print(i)
print(cnt - 2)  # 시작점 끝점 뺴고
