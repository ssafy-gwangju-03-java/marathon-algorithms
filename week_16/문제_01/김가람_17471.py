import sys
from itertools import combinations

N = int(sys.stdin.readline())
population = [0] + list(map(int, sys.stdin.readline().split()))

adjl = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    adjacent_node = list(map(int, sys.stdin.readline().split()))
    for j in range(1, 1 + adjacent_node[0]):
        adjl[i].append(adjacent_node[j])

def get_population_sum(num_list):
    return sum([population[num] for num in num_list])

def dfs(curr, visited, curr_section):
    visited[curr] = True

    for next in adjl[curr]:
        if not visited[next] and next in curr_section:  # 인접 노드가 방문 전이고, 같은 선거구 내에 있다면
            dfs(next, visited, curr_section)


min_diff = 100000

# 전체 구역을 나누는 모든 경우의 수를 조합으로 탐색
for i in range(1, int(N / 2) + 1):
    chosen_case_list = combinations([j for j in range(1, N + 1)], i)

    for chosen_case in chosen_case_list:
        blue = list(chosen_case)
        red = list({j for j in range(1, N + 1)} - set(blue))

        visited = [False] * (N + 1)

        dfs(blue[0], visited, blue)
        dfs(red[0], visited, red)

        # 각 선거구끼리 dfs 했는데 모두 방문처리가 되었다면 정답 갱신
        if not (False in visited[1:]):
            min_diff = min(min_diff, abs(get_population_sum(blue) - get_population_sum(red)))

print(min_diff if min_diff != 100000 else -1)
