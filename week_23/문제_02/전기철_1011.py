# 1011 fly me to the Alpha Centauri

t = int(input())

## 순서

## 1 1을 외곽에 두고 수가 늘어날때마다 2 2 3 3 4 4 ---를 사이드에 배치
## ex) 6 = 1 2 2 1 / 9 = 1 2 3 2 1 / 12 = 1 2 3 3 2 1

for tc in range(1, t + 1):
    x, y = map(int, input().split())
    cnt = 0
    add = 1
    dis = y - x
    now = 0

    while 1:
        if now >= dis:
            break
        now += add

        if cnt % 2: # 2회마다 1씩 늘려서 더하기
            add += 1
        cnt += 1

    print(cnt)
