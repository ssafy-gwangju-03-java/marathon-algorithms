# https://www.acmicpc.net/problem/22251

## Referenced
# https://moonsbeen.tistory.com/324

import sys

input = sys.stdin.readline

# 7-세그먼트 디스플레이별 LED 상태
display = [
    [1, 1, 1, 0, 1, 1, 1],  # 0
    [0, 0, 1, 0, 0, 0, 1],  # 1
    [0, 1, 1, 1, 1, 1, 0],  # 2
    [0, 1, 1, 1, 0, 1, 1],  # 3
    [1, 0, 1, 1, 0, 0, 1],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 0, 1, 1, 1, 1],  # 6
    [0, 1, 1, 0, 0, 0, 1],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
]


def num_to_digit(X):
    """
    숫자 X를 K자리의 배열로 채워서 반환
    """
    digit = []
    for x in str(X).zfill(K):
        digit.append(int(x))
    return digit


def is_reversable(source, target):
    """
    source, target 숫자의 세그먼트 LED 차이 개수를 구하고,
    그 개수가 P개 이하인지 여부를 반환
    """
    target = num_to_digit(target)
    count = 0

    for i in range(K):
        for j in range(7):
            if display[source[i]][j] != display[target[i]][j]:
                count += 1

    return count <= P


N, K, P, X = map(int, input().split())
digit = num_to_digit(X)
result = 0

for i in range(1, N + 1):
    # 1부터 N까지 자기 자신 X를 제외한 숫자를 P개 내로 반전시킬 수 있는지 확인
    if i != X and is_reversable(digit, i):
        result += 1

print(result)
