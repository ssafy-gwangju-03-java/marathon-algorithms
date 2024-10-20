# 2138 전구와 스위치
def switch(bulbs, i):
    for j in range(i-1, i+2):
        if 0 <= j < n:
            if bulbs[j] == '0': # 켜져있으면
                bulbs[j] = '1'  # 끄고
            else:   # 꺼져있으면
                bulbs[j] = '0' # 켜고

def solve(bulbs):
    cnt = 0
    for i in range(1, n):
        if bulbs[i-1] != target[i-1]:
            switch(bulbs, i)
            cnt += 1

    if bulbs == target:
        return cnt
    else:
        return -1

n = int(input())
current = list(input())
target = list(input())

# 첫 번째 스위치 안 누른 경우
ans1 = solve(current[:])    # solve 호출 2번째부터 영향 미치니까 얕은 복사 해야 함

# 첫 번째 스위치 누른 경우
switch(current, 0)
ans2 = solve(current)
if ans2 != -1:
    ans2 += 1 # 첫 번째 스위치 누른 거 추가해서

# Output
if ans1 != -1 and ans2 != -1:
    print(min(ans1, ans2))
elif ans1 != -1:
    print(ans1)
elif ans2 != -1:
    print(ans2)
else:
    print(-1)