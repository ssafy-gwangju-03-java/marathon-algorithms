# 센서
N = int(input())
K = int(input())

lst = list(map(int, input().split()))

lst.sort()
distance = []

# 집중국의 수가 센서의 수보다 클 때 센서마다 집중국 설치하면 됨
if K >= N:
    print(0)
# 그렇지 않을 때 계산
else:
    # 센서간 거리 차이 계산
    for i in range(N - 1):
        distance.append(lst[i + 1] - lst[i])
    distance.sort()

    # 거리 차이가 큰 부분 부터 집중국 분리
    for _ in range(K - 1):
        distance.pop()
    print(sum(distance))

    # 아래 코드로 위의 세줄 대체 가능
    # print(sum(distance[:N - (K - 1)]))