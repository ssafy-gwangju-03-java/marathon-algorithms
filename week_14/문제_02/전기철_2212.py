# 2212 센서
n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()

sensor = []
for i in range(n - 1):
    sensor.append(lst[i + 1] - lst[i])

sensor.sort()

ans = 0
for i in range(n - k):
    ans += sensor[i]
print(ans)

# 13164 행복유치원과 유사하게 k-1개의 벽을 세워 차이값을 하나씩 쳐내면 됨
# if k==2면 sort 전 sensor=[2,2,1,4] , sort후 sensor=[1,2,2,4]이고 4를 쳐내면 됨 -> 차이가 4인 두 값 사이에 벽을 침 