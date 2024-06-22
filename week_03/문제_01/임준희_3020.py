import sys
input = sys.stdin.readline

N, H = map(int, input().split())
graph = [0 for _ in range(H)]
for i in range(N):
    height = int(input())
    if i % 2 == 0:
        # 짝수 인덱스일 경우, 석순 처리
        graph[H-height] += 1
    if i % 2 == 1:
        # 홀수 인덱스일 경우, 종유석 처리
        graph[0] += 1
        graph[height] -= 1

# 누적합을 계산하기 위해 리스트 초기화
prefix = [0 for _ in range(H+1)]

# 누적합 계산
for i in range(H):
    prefix[i+1] = prefix[i] + graph[i]

# 첫 번째 요소를 제외하고 누적합 리스트를 다시 저장
prefix = prefix[1:]

print(min(prefix), prefix.count(min(prefix)))