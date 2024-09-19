# 14891 톱니바퀴

from collections import deque

q1 = deque(list(map(int, input())))
q2 = deque(list(map(int, input())))
q3 = deque(list(map(int, input())))
q4 = deque(list(map(int, input())))
k = int(input())
lst = [q1, q2, q3, q4]
asd = []  # 회전 명령
ans = 0
for _ in range(k):
    x, y = map(int, input().split())
    asd.append([x, y])
for c in asd:  # 회전 돌리기
    x, y = c
    x -= 1
    rotate = [0, 0, 0, 0]
    rotate[x] = y
    for i in range(x, 0, -1):
        if lst[i][6] != lst[i - 1][2]:
            rotate[i - 1] = rotate[i] * -1
        else:
            break
    for i in range(x, 3):
        if lst[i][2] != lst[i + 1][6]:
            rotate[i + 1] = rotate[i] * -1
        else:
            break
    for i in range(4):
        if rotate[i] == 1:
            x = lst[i].pop()
            lst[i].appendleft(x)
        elif rotate[i] == -1:
            x = lst[i].popleft()
            lst[i].append(x)
for i in range(4):
    ans += lst[i][0] * (2**i)
print(ans)
