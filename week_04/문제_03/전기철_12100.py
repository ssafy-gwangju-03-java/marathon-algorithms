# 12100 2048 (easy)
def go(x):  # 이동
    if x == 0:  # up
        for j in range(n):
            check = 0  # 현재 이동해서 겹쳐질 수 있는 인덱스 위치
            for i in range(1, n):
                if a[i][j]:  # 해당 칸에 블럭이 있을 시
                    now = a[i][j]  # 값 저장
                    a[i][j] = 0  # 0으로 변경
                    if (
                        a[check][j] == now
                    ):  # 만약 현재 칸 블럭과 이동 칸 블럭값이 같은 경우 (ex) 2   2) <- 합친다
                        a[check][j] = now * 2  # 합친다
                        check += (
                            1  # 합쳐서 이제 그 칸으로는 영향을 줄 수 없으므로 한칸 이동
                        )
                    elif a[check][j] == 0:  # 빈 칸이면 그 칸으로 이동
                        a[check][j] = now
                    else:  # 블럭값은 있지만 합칠 수 없는 경우 ( 2 4 / 4 2 이런 식)
                        check += 1  # 인덱스 한칸 이동 후 그 곳에 블럭값 적용
                        a[check][j] = now

    elif x == 1:  # down
        for j in range(n):
            check = n - 1
            for i in range(n - 2, -1, -1):
                if a[i][j]:
                    now = a[i][j]
                    a[i][j] = 0
                    if a[check][j] == now:
                        a[check][j] = now * 2
                        check -= 1
                    elif a[check][j] == 0:
                        a[check][j] = now
                    else:
                        check -= 1
                        a[check][j] = now
    elif x == 2:
        for i in range(n):
            check = 0
            for j in range(1, n):
                if a[i][j]:
                    now = a[i][j]
                    a[i][j] = 0
                    if a[i][check] == 0:
                        a[i][check] = now
                    elif a[i][check] == now:
                        a[i][check] = now * 2
                        check += 1
                    else:
                        check += 1
                        a[i][check] = now
    else:  # right
        for i in range(n):
            check = n - 1
            for j in range(n - 2, -1, -1):
                if a[i][j]:
                    now = a[i][j]
                    a[i][j] = 0
                    if a[i][check] == now:
                        a[i][check] = now * 2
                        check -= 1
                    elif a[i][check] == 0:
                        a[i][check] = now
                    else:
                        check -= 1
                        a[i][check] = now


def game(k):
    global a
    global mx
    chk = 0
    if k == 5: # 5번 이동시
        for i in a:
            temp = max(i) # 최대값 갱신
            if temp > mx:  # 최적화 과정 1
                mx = temp
                for j in range(5, 0, -1):# if 현재 최대값이 128이라고 하면 4번 이동했을 때 64가 만들어지지 않는 경우 기존 값을 넘어설 수 없음 -> 밑에서 return
                    deep[j] = temp
                    temp //= 2
        return
    for i in a:
        chk = max(chk, max(i))
    if deep[k] >= chk: # 현재 최대값에서 어떻게 다 움직이더라도 기존 최대값을 넘을 수 없는 경우 return
        return
    b = [item[:] for item in a] # 2차원 배열의 경우 내부까지 slice로 복사해야 깊은 복사로 가능 ( b=a[:] 이런식으로는 내부 값까지 복사가 안되서 a[][]가 바뀌면 b도 바뀌는 현상 발생)
    for i in range(4): # 백트래킹
        go(i) # 간다
        game(k + 1) # 게임 한번 돌린다
        a = [item[:] for item in b] # 다시 원상태로 복사


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
deep = [0 for _ in range(6)]
mx = 0
game(0)
print(mx)
