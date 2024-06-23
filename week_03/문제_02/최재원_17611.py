import sys
sys.stdin = open("../input.txt")

N = int(input())

points = []
for i in range(N):
    r, c = map(int, input().split())
    points.append((r + 500000, c + 500000))

vertical = [0] * 1000001
horizontal = [0] * 1000001

for i in range(N):
    r, c = points[i]
    nr, nc = points[(i + 1) % N]

    if r == nr:
        if c > nc:
            c, nc = nc, c
        vertical[c] += 1
        vertical[nc] -= 1
    elif c == nc:
        if r > nr:
            r, nr = nr, r
        horizontal[r] += 1
        horizontal[nr] -= 1

max_vertical = max_horizontal = 0

current = 0
for count in vertical:
    current += count
    if current > max_vertical:
        max_vertical = current

current = 0
for count in horizontal:
    current += count
    if current > max_horizontal:
        max_horizontal = current

print(max(max_vertical, max_horizontal))