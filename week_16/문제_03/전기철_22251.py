# 22251 빌런 호석
n, k, p, x = map(int, input().split())

# k자리 맞추기 + str 변환
if len(str(x)) < k:
    number = "0" * (k - len(str(x))) + str(x)
else:
    number = str(x)

lst = [
    "1111110",
    "0110000",
    "1101101",
    "1111001",
    "0110011",
    "1011011",
    "1011111",
    "1110000",
    "1111111",
    "1111011",
]
arr = [[] for _ in range(10)]

for i in range(10):
    for j in range(10):
        if i == j:  # 같으면 0 넣고
            arr[i].append(0)
        else:
            d = 0
            for h in range(7):
                if lst[i][h] != lst[j][h]:  # 다른 세그먼트 개수 넣기
                    d += 1
            arr[i].append(d)


def dfs(depth, cnt, number):  # 깊이 , 횟수 , 문자
    if depth >= len(number):
        if int(number) == x:
            return 0
        elif 1 <= int(number) <= n:
            return 1
        else:
            return 0

    ans, cur = 0, int(number[depth])
    for i in range(10):  # 모든 숫자를 대상으로 바꿔보면서 재귀탐색
        if cur != i and (arr[cur][i] <= cnt):
            dx = number[:depth] + str(i) + number[depth + 1 :]
            ans += dfs(depth + 1, cnt - arr[cur][i], dx)

        elif cur == i:
            ans += dfs(depth + 1, cnt, number)

    return ans


print(dfs(0, p, number))
