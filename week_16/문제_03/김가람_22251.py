import sys

N, K, P, X = map(int, sys.stdin.readline().split())

# LED[i] = i번째 숫자의 LED 중 켜져있으면 1, 꺼져있으면 0
LED = [
    0b1110111,
    0b0100100,
    0b1011101,
    0b1101101,
    0b0101110,
    0b1101011,
    0b1111011,
    0b0100101,
    0b1111111,
    0b1101111
]

diff = [[0] * 10 for _ in range(10)]

# diff[i][j] = 숫자 i에서 숫자 j로 바꿀 때 반전시켜야 할 LED의 갯수
for i in range(10):
    for j in range(10):
        diff[i][j] = str(bin(LED[i] ^ LED[j])).count('1')

"""
num_list = 현재 탐색중인 층 수
count = 지금까지 반전시킨 LED의 갯수
curr_idx = 현재 바꾸고자 하는 층수의 자릿수
"""
def dfs(num_list, count, curr_idx):
    global ans

    if count > P:
        return

    if curr_idx == K:
        curr_floor = int(''.join(map(str, num_list)))
        if 1 <= curr_floor <= N and curr_floor != X:
            ans += 1
        return

    for next in range(10):
        new_list = [num for num in num_list]
        curr = int(new_list[curr_idx])
        new_list[curr_idx] = str(next)
        dfs(new_list, count + diff[curr][next], curr_idx + 1)


ans = 0
dfs(list("0" * (K - len(str(X))) + str(X)), 0, 0)   # K = 2, X = 9일 때 input은 ["0", "9"]
print(ans)
