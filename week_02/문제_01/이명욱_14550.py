# 마리오 파티

def find(N, S, T, lst):
    # dp 초기 설정
    dp = [inf] * (N + 1)
    dp[0] = 0

    # T-1 번 주사위 굴리기
    for t in range(T - 1):
        # 임시 dp
        temp_dp = [0] + [inf] * N
        # dp 순회
        for i in range(N + 1):
            # dp의 값이 inf가 아닐 때 주사위 굴려서 이동
            if dp[i] != inf:
                for j in range(1, S + 1):
                    # 보드판 벗어 나지 않을 때
                    if i + j < N + 1:
                        # 주사위 눈금 수 만큼 이동, temp_dp 안에서 움직여서 나온 값과 dp[i]에서 j칸의 값 중 큰거 선택
                        temp_dp[i + j] = max(temp_dp[i + j], dp[i] + lst[i + j])
        # t번째 턴에서 움직여서 나온 값 반영
        dp = temp_dp
    # dp가 T-1번 주사위 굴린 결과
    # 한 번 더 주사위 굴릴때 마지막 칸 도착할 수 있는 범위 내에서 최댓값 구하기
    max_v = max(dp[N + 1 - S:])
    return max_v


inf = -1e9
while True:
    try:
        # N개의 정수, S 주사위에 적힌 최댓값, T 주사위 굴리는 횟수
        N, S, T = map(int, input().split())
        # 보드 첫번째 칸과 인덱스 맞추기 위해 0 미리 넣기
        lst = [0]
        # 입력받은 값이 0이면 반복문 탈출
        if N == 0:
            break
        # N개 입력 받을 때까지 반복
        while len(lst) < N + 1:
            lst.extend(list(map(int, input().split())))
        print(find(N, S, T, lst))
    except:
        break