# 세로 H, 가로 W
H, W = map(int, input().split())

# 블록 쌓인 높이(0<=heights<=H ) 왼쪽부터
heights = list(map(int, input().split()))

ans = 0

# 첫번째칸, 마지막칸 물 고일 수 x
for i in range(1, W-1):
    left_max = max(heights[:i]) # 현재 블록 왼쪽에 있는 블록들 중 최대 높이
    right_max = max(heights[i+1:]) # 현재 블록의 오른쪽에 있는 블록들 중 최대 높이

    # 왼쪽 최대 높이와 오른쪽 최대 높이 중 더 낮은 값 고르기
    possible = min(left_max, right_max)

    # 현재 블록 높이가 possible보다 낮으면 빗물 가능
    if heights[i] < possible:
        ans += possible - heights[i]


print(ans)