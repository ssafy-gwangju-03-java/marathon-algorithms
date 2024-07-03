# 나무 재테크

'''
5 2 6
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
'''
from pprint import pprint
from collections import deque
import sys

input = sys.stdin.readline

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def Season():
    for i in range(N):
        for j in range(N):
            tree_lst = tree_age[i][j]
            if tree_lst:
                amount = 0
                for _ in range(len(tree_lst)):
                    tree = tree_lst.popleft()
                    # 자신의 나이만큼 양분을 먹을 수 있을 때
                    if ground[i][j] >= tree:
                        ground[i][j] -= tree
                        tree_lst.append(tree + 1)
                        

                    # 자신의 나이만큼 양분을 먹을 수 없을 때
                    # 나무는 죽고 양분으로 변하게 됨
                    # 여름으로 넘어감
                    else:
                        amount += (tree // 2)
                
                ground[i][j] += amount
                        

    # 가을 & 겨울
    for i in range(N):
        for j in range(N):
            # 겨울
            ground[i][j] += A_array[i][j]

            # 가을
            for tree in tree_age[i][j]:
                # 나무의 나이가 5의 배수일 때
                if tree % 5 == 0:
                    for d in range(8):
                        ni = i + di[d]
                        nj = j + dj[d]

                        if 0 <= ni < N and 0 <= nj < N:
                            tree_age[ni][nj].appendleft(1)
    
N, M, K = map(int, input().split())

# 나무 위치의 양분
ground = [[5] * N for _ in range(N)]

A_array = [list(map(int, input().split())) for _ in range(N)]


# 나무의 나이를 저장할 리스트
tree_age = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    # (x, y) : 나무의 위치
    # z : 나무의 나이
    x, y, z = map(int, input().split())
    tree_age[x - 1][y - 1].append(z)

# pprint(tree_age)
for _ in range(K):
    Season()

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(tree_age[i][j])

print(cnt)