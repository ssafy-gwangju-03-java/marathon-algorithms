import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [input().strip() for _ in range(N)]


def make_set(n):
    return list(range(n))


def find_set(x):
    # 대표가 자신이면 반환
    if x == p[x]:
        return x

    # 자신이 아니면 부모의 대표 찾기
    p[x] = find_set(p[x])

    return p[x]


def union(curr, target):
    # 집합의 대표찾기
    a = find_set(curr)
    b = find_set(target)

    # 대표가 다르면 합치기
    if a != b:
        p[b] = a


# N * M 개 길이의 리스트 생성
p = make_set(N * M)

# 0번부터 11번 집합을 순회하며 합치기
for i in range(N):
    for j in range(M):
        # 0번부터 N * M 번 집합
        curr = (i * M) + j

        # 4가지 방향에 따라 현재 집합과 합칠 집합 정하기
        if arr[i][j] == 'U':
            target = curr - M
        elif arr[i][j] == 'D':
            target = curr + M
        elif arr[i][j] == 'L':
            target = curr - 1
        else:
            target = curr + 1

        # 합치기
        union(curr, target)

# 전체 경로압축
for i in range(N * M):
    find_set(i)

# 대표자 수 = safe_zone 수
print(len(set(p)))
