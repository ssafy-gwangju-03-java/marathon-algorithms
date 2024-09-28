# 14719 빗물
import sys
input = sys.stdin.readline

def solve():
    ans = 0     # 빗물 안 고였을 때
    # 탐색할 시작위치
    start = 0
    end = w - 1
    # start end 사이 값을 세서 ans 플러스
    while start < end:
        if arr[start] <= arr[end]:  # start, end 높이 비교
            current = arr[start]    # start부터 시작
            start += 1
            while start < end and arr[start] < current: # current 보다 낮은 칸 세기
                ans += current - arr[start]
                start += 1

        else:
            current = arr[end]  # end부터 시작
            end -= 1
            while start < end and arr[end] < current:   # current 보다 낮은 칸 세기
                ans += current - arr[end]
                end -= 1

    return ans


h, w = map(int, input().split())    # h:세로길이, w:가로길이
arr = list(map(int, input().split()))   # 높이 정보

print(solve())