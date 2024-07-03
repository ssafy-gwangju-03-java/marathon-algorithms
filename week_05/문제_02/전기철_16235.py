from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

n, m, k = map(int, input().split())
A_map = [list(map(int, input().split())) for _ in range(n)]
arr = [[5] * n for _ in range(n)]
lst = [[deque() for _ in range(n)] for _ in range(n)]  # deque의 이유 -> popleft와 appendleft(가을) 쓰려고

for _ in range(m):
    y, x, z = map(int, input().split())
    x -= 1
    y -= 1  # 시작 좌표가 1,1이라 했으므로 1씩 빼서 좌표에 적용
    lst[y][x].append(z)

for _ in range(k):
    dead = []  # 여름용 죽은 나무 저장
    fall_tree = []  # 가을용 번식 나무 저장

    # 봄
    for y in range(n):
        for x in range(n):
            if lst[y][
                x
            ]:  # sort를 안해도 되는 이유 -> 첫 탐색은 (입력으로 주어지는 나무의 위치는 모두 서로 다름) 조건을 통해 각각 하나씩이므로 필요없음
                # 번식 후 과정 -> 번식하면 나이가 1인 나무가 퍼지므로 appendleft로 앞에다가 넣어버리면 정렬된 상태 유지 가능
                for i in range(len(lst[y][x])):
                    tree = lst[y][x].popleft()
                    if tree > arr[y][x]:  # 나이가 양분보다 많으면 죽음
                        dead.append((y, x, tree))
                        continue
                    arr[y][x] -= tree  # 나무가 양분 먹고
                    lst[y][x].append(tree + 1)  # 나이 1살 상승
                    if not (tree + 1) % 5:  # 나이가 5의 배수가 된 경우 번식 준비
                        fall_tree.append((y, x))

    # 여름
    for y, x, tree in dead:  # 죽은 나무들 양분화
        arr[y][x] += tree // 2

    # 가을
    for y, x in fall_tree:  # 가을 나무들 번식
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                lst[ny][nx].appendleft(
                    1
                )  # appendleft를 통해 앞에다가 넣음(어린 나무들부터 봄에 처리해야하므로)

    # 겨울
    for y in range(n):
        for x in range(n):
            arr[y][x] += A_map[y][x]

cnt = 0
for y in range(n):
    for x in range(n):
        cnt += len(lst[y][x])  # 나무 개수
print(cnt)
