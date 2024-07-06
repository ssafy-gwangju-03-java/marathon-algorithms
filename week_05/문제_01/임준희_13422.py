def solve(N, M, K, houses):
    # N과 M이 같은 경우 처리
    if N == M:
        return 1 if sum(houses) < K else 0
    
    # 원형 리스트를 만들기 위해 집 리스트를 두 번 반복
    circle = houses + houses[:M-1]
    
    # 초기 윈도우 합 계산
    window_sum = sum(circle[:M])
    
    # 가능한 방법의 수 초기화
    count = 1 if window_sum < K else 0
    
    # 슬라이딩 윈도우
    for i in range(N-1):
        # 윈도우에서 첫 번째 집을 제거하고 새로운 집을 추가
        window_sum = window_sum - circle[i] + circle[i+M]
        
        # K 미만인 경우 유효한 방법으로 카운트
        if window_sum < K:
            count += 1
    
    return count

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))
    print(solve(N, M, K, houses))