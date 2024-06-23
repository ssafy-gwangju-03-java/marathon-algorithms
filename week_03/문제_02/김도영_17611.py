# 직각다각형

"""
input
4
-1 -1
-1 1
1 1
1 -1

output
2
"""

# n : 꼭짓점의 갯수
n = int(input())

x = [0] * 100001
y = [0] * 100001

for i in range(n):
    x[i], y[i] = map(int, input().split())

garo = [0] * 1000001
sero = [0] * 1000001
# +500,000은 양수 인덱스로 바꾸기 위함
for i in range(n - 1):
    # 수직 선분
    if x[i] == x[i + 1]:
        sero[max(y[i], y[i + 1]) + 500000] -= 1
        sero[min(y[i], y[i + 1]) + 500000] += 1

    # 수평 선분
    elif y[i] == y[i + 1]:
        garo[max(x[i], x[i + 1]) + 500000] -= 1
        garo[min(x[i], x[i + 1]) + 500000] += 1

# 마지막 선분과 처음 선분 연결
if x[0] == x[n - 1]:
    sero[max(y[0], y[n - 1]) + 500000] -= 1
    sero[min(y[0], y[n - 1]) + 500000] += 1

elif y[0] == y[n - 1]:
    garo[max(x[0], x[n - 1]) + 500000] -= 1
    garo[min(x[0], x[n - 1]) + 500000] += 1

sero_cnt = 0
garo_cnt = 0
sero_y = -500001
garo_x = -500001
# 교차 횟수 누적합
for i in range(1000001):
    sero_cnt += sero[i]
    sero[i] = sero_cnt
    sero_y = max(sero[i], sero_y)

    garo_cnt += garo[i]
    garo[i] = garo_cnt
    garo_x = max(garo[i], garo_x)

# 가로와 세로 중 최댓값 출력
print(max(sero_y, garo_x))