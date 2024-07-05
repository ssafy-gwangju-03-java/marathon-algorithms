# 봄에는 나이만큼 양분 먹고, 나이 +1 :
# 어린 나무 부터, 양분 부족하면 나무 죽음
def spring():
    # 어린 나무부터 양분 먹을거니까 trees sort
    trees.sort(key=lambda x: x[2])
    i = -1
    for tree in trees:
        i += 1
        r, c, age = tree[0] - 1, tree[1] - 1, tree[2]
        # 죽은 나무는 패스
        if age < 0:
            continue
        # 양분이 충분하면
        # 악 nutrient는 겨울에 추가할 애고 기본 양분은 따로 한칸당 5씩;;;;;;;;;;;
        if land[r][c] >= age:
            print(111)
            # 양분 먹고 나이 ++
            land[r][c] -= age
            age += 1
            print('age', age)
            trees[i][2] = age
            print('양분먹고 나이든 나무', trees)
        # 양분이 모자라면
        else:
            print(222)
            # 나무 죽음
            dead.append((r, c, age))
            # trees[i][2] = -1
            trees.remove(trees[i])
            print('나무죽고', trees)
            print('죽은나무', dead)


# 여름에는 죽은 나무 -> 양분 : 나이 // 2 만큼 추가
def summer():
    global dead
    i = -1
    for tree in dead:
        i += 1
        r, c, age = tree[0], tree[1], tree[2]
        land[r][c] += age // 2
        dead.remove(dead[i])


# 가을에는 번식
# -> 나무 나이 5의 배수, 인접 8개칸에 나이 1인 나무 추가 (땅 범위 내에서)
def autumn():
    for tree in trees:
        r, c, age = tree[0] - 1, tree[1] - 1, tree[2]
        if age % 5 != 0:
            continue
        # 인접 8개칸에 나이 1인 나무 추가하기
        print('번식')
        for i in range(-1, 2):
            for j in range(-1, 2):
                # 범위 내에 있으면 + 자기자신빼고
                if 0 <= r + i < N and 0 <= c + j < N:
                    if i == 0 and j == 0:
                        continue
                    trees.append([r + i, c + j, 1])
        print('번식 후 나무', trees)


# 겨울에는 nutrient[r][c] 만큼의 양분을 land의 (r,c) 위치에 추가
def winter():
    for r in range(N):
        for c in range(N):
            land[r][c] += nutrient[r][c]


# N*N 땅, 나무 M개, K년 후 살아남은 나무.
N, M, K = map(int, input().split())
# 겨울에 각 칸에 추가되는 양분의 양 A[r][c]
nutrient = [list(map(int, input().split())) for _ in range(N)]
# 나무 M개 r,c,나이
# 땅 한 칸에 나무 여러 개 가능
trees = [list(map(int, input().split())) for _ in range(M)]

# 봄에는 나이만큼 양분 먹고, 나이 +1 : 어린 나무 부터, 양분 부족하면 나무 죽음
# 여름에는 죽은 나무 -> 양분 : 나이 // 2 만큼 추가
# 가을에는 번식 -> 나무 나이 5의 배수, 인접 8개칸에 나이 1인 나무 추가 (땅 범위 내에서)
# 겨울에는 nutrient[r][c] 만큼의 양분을 (r,c) 위치에 추가
dead = []
# 기본 양분
land = [[5] * N for _ in range(N)]

# K년동안 4계절 지날 것
for y in range(K):
    spring()
    summer()
    autumn()
    winter()

print(len(trees))
