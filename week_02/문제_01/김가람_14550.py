N = 0
S = 0
T = 0
arr_cnt = 0
arr = []

def dp(arr, N, S, T):
    # 해당 움직임의 코인의 최댓값을 Memoization 해줄 2차원 행렬
    # 행 : 움직임의 회차 (T-1행)
    # - T회차 움직임의 최댓값은 T-1회차 움직임을 기록한 행의 [마지막:마지막-S:-1]열에서 판단할 예정이므로 행은 T-1개만 필요
    # 열 : 해당 움직임에서 획득할 코인, N개의 열 필요
    # 코인의 절댓값은 10000 이하
    memo = [[-10001] * N for _ in range(T-1)]

    # 첫번째 움직임 초기값 저장
    memo[0][0:S] = arr[0:S]

    # 두번째 움직임부터 메모이제이션
    for i in range(1, T-1):
        for j in range(N):
            max_value = -10001

            # 전 회차의 열로부터 S 이하의 칸씩 이동 가능
            for k in range(1, S+1):
                if j-k >= 0 and memo[i-1][j-k] > -10001:
                    # 지난 회차(i-1)의 j-k번째 열에서 얻은 코인 값 + j번째 열의 코인값을 더해 현재 회차(i번째)의 최댓값을 판별
                    max_value = max(max_value, memo[i-1][j-k] + arr[j])

            # 움직이지 못한 칸은 그대로 -10001
            memo[i][j] = max_value

    # T-1회차 움직임에서 END에 도달할 수 있는 열들만 고른 후 그 열들 가운데에서 최댓값 리턴
    return max(memo[T-2][N-S])


while True:
    input_str = input()

    # 입력받은 원소 갯수가 N개에 도달하면 일처리
    if arr_cnt == N:
        if arr:
            # N개 원소가 다 차면 DP 돌린 후 초기화
            print(dp(arr, N, S, T))

            # 갯수와 배열 초기화
            arr_cnt = 0
            arr = []
        if input_str == "0":
            break
        else:
            # 배열이 비어있다면 N, S, T 입력
            N, S, T = map(int, input_str.split())
    else:
        # 현재까지 입력받은 원소 갯수가 N개에 도달하지 못했다면 계속 입력받기
        arr += list(map(int, input_str.split()))
        arr_cnt += len(input_str.split())
