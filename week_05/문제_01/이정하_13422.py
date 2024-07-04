T = int(input())

for tc in range(1, T + 1):
    # 집 N개, 돈훔칠 연속 M 집, 방범작동 돈 K원
    # M <= 10만, M<=N, K<=10억 => 완탐 x
    N, M, K = map(int, input().split())
    money = list(map(int, input().split()))  # 단, 집은 연결되어있다.
    if N == M:
        # 경우의 수가 1가지
        print(1 if sum(money) < K else 0)
        continue
        # else:
    sum_m = sum(money[:M])  # 처음 M 개의 집의 돈 합
    cnt = 0
    if sum_m < K:
        cnt += 1  # 첫번째 sum_m이 조건 만족하면 cnt ++

    for i in range(1, N):
        # 이전 집의 돈을 빼고 다음 집의 돈을 더해줌
        # 이번차례에서 money의 i-1번째 인덱스에 있는 돈을 빼줘야 함 : 이게 맨 앞칸
        # i번보다 M-1번 뒤에 있는 애가 더해져야 함 : 이게 i번부터 M번쨰 있는 돈, 원형이랑서 %N
        sum_m = sum_m - money[i - 1] + money[(i + M - 1) % N]
        if sum_m < K: # 갱신된 합계가 K보다 작은지 확인하자
            cnt += 1
    print(cnt)

'''
맞왜틀
T = int(input())
for tc in range(1, T + 1):
    # 집 N개, 돈훔칠 연속 M 집, 방범작동 돈 K원
    # M <= 10만, M<=N, K<=10억 => 완탐 x
    N, M, K = map(int, input().split())
    money = list(map(int, input().split()))  # 단, 집은 연결되어있다.
    if N == M:
        # 경우의 수가 1가지
        print(1 if sum(money) < K else 0)
        continue
    # else:
    sum_m = 0  # M 개의 집의 돈 합
    cnt = 0
    mth_houses = [0] * (N + 2)
    # N-1번째, N번째, 첫번째 집 돈 합 M개
    mth_houses[0] = money[0] + sum(money[i] for i in range(N - 1, N - M, -1))
    # mth_houses[1] = money[1] + money[0] + money[N - 1]

    for i in range(1, N):
        sum_m = mth_houses[i - 1]
        if sum_m < K:
            cnt += 1
        mth_houses[i] = sum_m - money[i - M] + money[i]
    print(cnt)
'''