from collections import defaultdict


def spring_and_summer():
    global trees
    new_trees = defaultdict(list)  # 새로운 나무들을 저장
    dead = []  # 죽은 나무들 저장

    # 모든 나무들에 대해서 처리
    for (r, c), ages in trees.items():
        ages.sort()  # 어린 순서대로 정렬
        survived = []  # 살아남은 나무들의 나이 목록

        # 해당 위치의 모든 나무들에 대해서 처리
        for age in ages:
            if land[r][c] >= age:  # 양분이 충분하면
                land[r][c] -= age  # 양분을 먹고
                survived.append(age + 1)  # 나이가 1 증가한 나무를 살아남은 목록에 추가
            else:  # 양분이 부족하면
                dead.append((r, c, age))  # 죽은 나무 목록에 추가

        new_trees[(r, c)] = survived  # 갱신된 살아남은 나무들의 목록을 저장

    # 죽은 나무들을 처리하여 양분으로 변환
    for r, c, age in dead:
        land[r][c] += age // 2

    trees = new_trees  # 나무들을 갱신된 나무 목록으로 업데이트


def autumn():
    new_trees = defaultdict(list)  # 새로 생성된 나무들을 저장할 defaultdict 선언

    # 모든 나무들에 대해서 처리
    for (r, c), ages in trees.items():
        for age in ages:
            if age % 5 == 0:  # 나이가 5의 배수인 경우
                # 인접한 8개의 칸에 나이 1인 나무를 추가
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            new_trees[(nr, nc)].append(1)  # 나이가 1인 나무를 추가함

    # 새로 생성된 나무들을 원래 나무 목록에 추가
    for key, value in new_trees.items():
        trees[key].extend(value)


def winter():
    for r in range(N):
        for c in range(N):
            land[r][c] += nutrient[r][c]  


# 입력 처리
N, M, K = map(int, input().split())  # 땅의 크기 N, 나무의 수 M, 시뮬 반복할 횟수 K 입력
nutrient = [list(map(int, input().split())) for _ in range(N)]  # 각 칸에 추가되는 양분 정보 입력
trees = defaultdict(list)  # 나무들을 저장할 defaultdict 선언
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[(x - 1, y - 1)].append(z)  # 나무의 위치와 나이를 나무 목록에 추가

land = [[5] * N for _ in range(N)] 

# K년 동안 4계절을 반복할 것
for _ in range(K):
    spring_and_summer()
    autumn()
    winter()

# 살아남은 나무의 수를 출력
result = sum(len(ages) for ages in trees.values())
print(result)

"""
from collections import deque


# 봄에는 나이만큼 양분 먹고, 나이 +1 : 어린 나무 부터, 양분 부족하면 나무 죽음
# 여름에는 죽은 나무 -> 양분 : 나이 // 2 만큼 추가
def spring_and_summer():
    global trees
    dead = []

    # 모든 나무에 대해서
    for (r, c) in list(trees.keys()):  # keys()를 리스트로 변환해서 순회해야 함 => 그래야 동시에 딕셔너리 변경해도 문제 없음
        tree_ages = trees[(r, c)]  # 해당 위치의 나무들의 나이 목록
        new_tree_ages = deque()  # 새로운 나이 목록 저장

        # 해당 위치의 모든 나무들에 대해서
        while tree_ages:
            age = tree_ages.popleft()  # 가장 앞의 나이 가져오기
            if land[r][c] >= age:  # 양분이 충분하면
                land[r][c] -= age  # 양분을 먹고
                new_tree_ages.append(age + 1)  # 나이 먹고 새 목록에 추가
            else:  # 양분이 부족하면
                dead.append((r, c, age))  # 죽은 나무 기록

        # 해당 위치에 남은 나무들의 새로운 나이 목록 갱신
        if new_tree_ages:
            trees[(r, c)] = new_tree_ages  # 남은 나무들 나이 목록을 갱신
        else:
            del trees[(r, c)]  # 남은 나무가 없으면 해당 위치의 나무들을 제거

    # 죽은 나무는 양분으로
    for r, c, age in dead:
        land[r][c] += age // 2


# 가을에는 번식
# -> 나무 나이 5의 배수, 인접 8개칸에 나이 1인 나무 추가 (땅 범위 내에서)
def autumn():
    new_trees = {}  # 새로 생성된 나무들 딕셔너리로 관리

    # 모든 나무에 대해
    for (r, c), ages in trees.items():
        for age in ages:
            if age % 5 == 0:
                # 인접 8개칸에 나이 1인 나무 추가하기
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        # 자기자신 빼고
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        # 범위 내에 있으면
                        if 0 <= nr < N and 0 <= nc < N:
                            if (nr, nc) in new_trees:
                                new_trees[(nr, nc)].appendleft(1)  # 이미 있으면 나이 1 ++
                            else:
                                new_trees[(nr, nc)] = deque([1])  # 처음이면 새 deque 만들고 추가

    # 새로운 나무들을 원래 나무 딕셔너리에 추가하기
    for key, value in new_trees.items():
        if key in trees:
            trees[key].extend(value)  # 이미 있으면 기존 나무들과 합침
        else:
            trees[key] = value  # 처음이면 새로 나무 추가함


# 겨울에는 nutrient[r][c] 만큼의 양분을 land의 (r,c) 위치에 추가
def winter():
    for r in range(N):
        for c in range(N):
            land[r][c] += nutrient[r][c]  # 겨울에 추가되는 양분을 더함


# 입력 처리
N, M, K = map(int, input().split())
# 겨울에 각 칸에 추가되는 양분의 양 A[r][c]
nutrient = [list(map(int, input().split())) for _ in range(N)]
trees = {}  # 나무를 딕셔너리에 저장하자

# 나무 정보를 tree 딕셔너리로
for _ in range(M):
    r, c, age = map(int, input().split())
    if (r - 1, c - 1) in trees:
        trees[(r - 1, c - 1)].append(age)  # 나무 이미 있으면 그 위치의 deque에 추가
    else:
        trees[(r - 1, c - 1)] = deque([age])  # 처음이면 새 deque 만들어서 추가

# 기본 양분
land = [[5] * N for _ in range(N)]

# K년동안 4계절 지날 것
for _ in range(K):
    spring_and_summer()
    autumn()
    winter()

# 생존한 나무 개수
result = sum(len(ages) for ages in trees.values())
print(result)

'''
# 봄에는 나이만큼 양분 먹고, 나이 +1 :
# 어린 나무 부터, 양분 부족하면 나무 죽음
def spring():
    dead = []
    # 어린 나무부터 양분 먹을거니까 trees sort
    trees.sort(key=lambda x: x[2])
    print('sorted trees', trees)
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
            # trees.remove(trees[i])
            print('나무죽고', trees)
            print('죽은나무', dead)
    for r, c, age in dead:
        trees.remove([r + 1, c + 1, age])


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
        r, c, age = tree[0], tree[1], tree[2]
        if age % 5 != 0:
            continue
        # 인접 8개칸에 나이 1인 나무 추가하기
        print('번식', tree)
        for i in range(-1, 2):
            for j in range(-1, 2):
                # 범위 내에 있으면 + 자기자신빼고
                if 0 < r + i <= N and 0 < c + j <= N:
                    if i == 0 and j == 0:
                        continue
                    trees.append([r + i, c + j, 1])
        print('번식 후 나무', trees)


# 겨울에는 nutrient[r][c] 만큼의 양분을 land의 (r,c) 위치에 추가
def winter():
    for r in range(N):
        for c in range(N):
            land[r][c] += nutrient[r][c]
    print('---')


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
    print('year', y + 1, 'K=', K)
    spring()
    summer()
    autumn()
    winter()
    print('------')

print(len(trees))
'''
"""