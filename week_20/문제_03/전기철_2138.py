# 2138 전구와 스위치


# 풀이 -> 0번 전구를 누른대 or 안누른다로 케이스를 나누면 그거에 맞춰서 1번부터 쭉 눌러야하므로
# 이 두가지 케이스만 고려해서 풀이 진행
def on(lst, cnt):
    for i in range(1, n - 1):
        if lst[i - 1] != answer[i - 1]:
            cnt += 1
            for j in range(i - 1, i + 2):
                lst[j] = (lst[j] + 1) % 2
    if lst[n - 1] != answer[n - 1]:  # 처음과 동일하게 따로처리
        cnt += 1
        lst[n - 2] = (lst[n - 2] + 1) % 2
        lst[n - 1] = (lst[n - 1] + 1) % 2
    if lst == answer:
        return cnt
    else:
        return -1


n = int(input())

lston = list(map(int, input()))  # 0번 킬 리스트

lstoff = lston[:]  # 0번 끌 리스트

lston[0] = (lston[0] + 1) % 2  # 0번 켰을때 반전되는 스위치
lston[1] = (lston[1] + 1) % 2

answer = list(map(int, input()))

if lstoff == answer:
    print(0)
else:
    cnt = on(lstoff, 0)
    if cnt != -1:
        print(cnt)
    else:
        cnt = on(lston, 1)
        print(cnt)  # 여기서도 -1이면 둘다안되니까 -1 출력
