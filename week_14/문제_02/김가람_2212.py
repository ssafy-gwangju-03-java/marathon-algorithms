import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))
sensors.sort()

# 행복 유치원과 똑같이 풀었음
diff = []
for i in range(1, N):
  diff.append(sensors[i] - sensors[i - 1])
diff.sort(reverse=True)

print(sum(diff[K-1:]))