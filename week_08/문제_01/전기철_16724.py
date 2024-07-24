import sys

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
lst = [list(map(str, input())) for _ in range(n)]


def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])

    return p[x]


def union(now, nxt):
    a = find(now)
    b = find(nxt)

    if a != b:
        p[b] = a


p = [i for i in range(n * m)]

for y in range(n):
    for x in range(m):
        now = y * m + x  # 0~n*m

        if lst[y][x] == "U":
            nxt = now - m  # 위로 간다 -> y-=1 -> now-=m
        elif lst[y][x] == "D":
            nxt = now + m
        elif lst[y][x] == "L":
            nxt = now - 1
        else:
            nxt = now + 1

        union(now, nxt)

for i in range(n * m):  # 경로압축 해줘야함
    find(i)

print(len(set(p)))
