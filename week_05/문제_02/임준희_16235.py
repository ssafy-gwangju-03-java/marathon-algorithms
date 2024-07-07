N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 나무 정보 저장
trees = {}
for _ in range(M):
    x, y, z = map(int, input().split())
    if (x-1, y-1) not in trees:
        trees[(x-1, y-1)] = []
    trees[(x-1, y-1)].append(z)

# 양분 정보 초기화
nutrient = [[5] * N for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# K년 동안 반복
for _ in range(K):
    # 봄, 여름: 나무가 양분을 먹고 나이가 증가하거나 죽음
    for (x, y), ages in list(trees.items()):
        ages.sort()  # 나이 순으로 정렬
        new_ages = []
        dead = 0
        for age in ages:
            if nutrient[x][y] >= age:
                nutrient[x][y] -= age
                new_ages.append(age + 1)
            else:
                dead += age // 2
        trees[(x, y)] = new_ages
        
        # 여름: 죽은 나무가 양분으로 변함
        nutrient[x][y] += dead
    
    # 가을: 나무 번식
    new_trees = {}
    for (x, y), ages in trees.items():
        for age in ages:
            if age % 5 == 0:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if (nx, ny) not in new_trees:
                            new_trees[(nx, ny)] = []
                        new_trees[(nx, ny)].append(1)
        if (x, y) not in new_trees:
            new_trees[(x, y)] = []
        new_trees[(x, y)].extend(ages)
    trees = new_trees
    
    # 겨울: S2D2가 양분 추가
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += A[i][j]

# 살아남은 나무의 수 계산
total_trees = sum(len(ages) for ages in trees.values())
print(total_trees)