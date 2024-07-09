from itertools import combinations


def worldcup(rnd):
    global cnt
    if rnd == 15:
        cnt = 1  # 15라운드까지 왔으면 가능성이 있으므로 이제 1로 바꿈
        for i in lst:
            if sum(i):
                cnt = 0  # 합이 0이 아닌 경우 문제가 생긴 것이므로 0으로 바꿈
                break
        return
    red, blue = soccer[rnd]
    for x, y in [[0, 2], [1, 1], [2, 0]]:  # (승,패) / (무,무) / (패,승)
        if lst[red][x] and lst[blue][y]:  # 둘다 뺄수있으면 돌려보기
            lst[red][x] -= 1
            lst[blue][y] -= 1
            worldcup(rnd + 1)
            lst[red][x] += 1
            lst[blue][y] += 1


soccer = list(combinations((0, 1, 2, 3, 4, 5), 2))  # 6개팀을 2팀끼리 매칭하는 모든 경우의수 - 15개
for _ in range(4):
    line = list(map(int, input().split()))
    lst = [line[i : i + 3] for i in range(0, 16, 3)]  # 3개씩 끊어서 저장하려고
    cnt = 0  # worldcup 통과하면 1로 바뀔 예정
    worldcup(0)
    print(cnt, end=" ")
