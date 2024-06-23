n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

# 중간값, 전체범위 설정
mid = 500_000
total = mid * 2 + 1

def solve(hv):
    line = [0] * total # 교차 횟수 계산할 배열

    for cur in range(hv, n, 2):
        next = (cur + 1) if cur + 1 !=n else 0 # 다음 꼭지점 계산

        j = 0 
        if arr[cur][0] == arr[next][0]: # 수직 선분일 경우
            j =1 # y좌표를 사용해서 구간 설정

        min_p, max_p = sorted([arr[cur][j],arr[next][j]]) # 현재 구간의 최소값, 최대값 구하기
        line[min_p + mid] += 1 # 구간의 시작점에 +1 
        line[max_p + mid] -=1 # 끝점에 -1

    ans, tot = 0, 0 # 누적 교차 횟수를 계산해서 최대 값 찾기
    for i in line:
        tot += i
        ans = max(ans, tot)
    return ans
# 수평선 h와 수직선 v의 최대 교차 횟수를 계산해서 최댓값 출력
ans = max(solve(0), solve(1))
print(ans)