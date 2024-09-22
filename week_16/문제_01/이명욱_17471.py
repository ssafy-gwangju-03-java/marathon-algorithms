import sys, itertools, collections


def bfs(same):
    start = same[0]
    q = collections.deque([start])
    visited = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += pp[v]
        for u in g[v]:
            if u not in visited and u in same:
                q.append(u)
                visited.add(u)
    return _sum, len(visited)


# 정점의 수, 인구 수 입력
n = int(sys.stdin.readline().strip())
pp = [int(x) for x in sys.stdin.readline().split()]

# 그래프를 인접 리스트 형태로 저장
g = collections.defaultdict(list)
result = float('inf')

# 각 정점과 연결된 다른 정점들 입력
for i in range(n):
    _input = [int(x) for x in sys.stdin.readline().split()]
    for j in range(1, _input[0] + 1):
        g[i].append(_input[j] - 1)

# 그룹을 나누는 조합
for i in range(1, n // 2 + 1):
    combis = list(itertools.combinations(range(n), i))
    for combi in combis:
        # 첫번째 그룹
        sum1, v1 = bfs(combi)
        # 두번째 그룹
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        # -> 2번의 bfs를 통해 모든 노드가 방문하는지 확인

        # 전체 정점의 수와 같다면
        if v1 + v2 == n:
            # 최소값 비교 후 저장
            result = min(result, abs(sum1 - sum2))

# 결과 출력
if result != float('inf'):
    print(result)
else:
    print(-1)

# 참고: https://cotak.tistory.com/66 [TaxFree:티스토리]