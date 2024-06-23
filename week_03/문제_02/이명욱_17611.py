# 직각 다각형
# 참고 : https://davincicoding.co.kr/101

# x 좌표 혹은 Y 좌표가 바뀌는 부분 체크
# 바뀌는 지점 이후에 겹치는 부분 1 증가

def find(xy):
    line = [0] * 1000001
    for now in range(xy, N, 2):
        # xy가 1일 경우 마지막 좌표와 처음 좌표 비교하는 경우 고려
        if now + 1 != N:
            nxt = now + 1
        else:
            nxt = 0

        # x 축이 같을 경우 y축 비교
        idx = 0
        if lst[now][0] == lst[nxt][0]:
            idx = 1

        # 작은 값에는 + 1 큰 값에는 - 1
        min_v, max_v = sorted([lst[now][idx], lst[nxt][idx]])
        # x, y좌표가 음수일 경우가 있으니 범위 맞춰주기
        line[min_v + 500000] += 1
        line[max_v + 500000] -= 1

    # 누적합 구하기
    ans, total = 0, 0
    for i in range(len(line)):
        total += line[i]
        ans = max(ans, total)
    return ans


N = int(input())

lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

# 수평축, 수직축의 최대값 구해 그 중에서 큰 값 출력
result = max(find(0), find(1))
print(result)