import sys
input = sys.stdin.readline

while True:
    try:
        # 입력 받기
        N, S, T = map(int, input().split())
        
        # 보드 초기화
        board = []
        cnt = 0
        while cnt < N:
            tmp = list(map(int, input().split()))
            cnt += len(tmp)
            board.extend(tmp)
        
        # DP 배열 초기화
        dp = [[-3000000]*(N+1) for _ in range(T)]
        
        # 첫 번째 턴의 초기화
        for i in range(N+1):
            dp[0][i] = 0
        
        # DP 배열 채우기
        for i in range(T):
            for j in range(1, S+1):
                for k in range(N+1):
                    # 이전 턴이 존재하고, 현재 칸에서 이동 가능한 경우에만 계산
                    if i-1 < 0 or k-j < 0:
                        continue
                    # 현재 턴에서의 최대 이동 거리를 넘어가는 경우는 계산하지 않음
                    if i*S < k:
                        continue
                    # DP 갱신: 이전 턴의 값과 현재 칸의 보상을 더한 값 중 최댓값 저장
                    dp[i][k] = max(dp[i][k], dp[i-1][k-j] + board[k-1])
        
        # 마지막 턴에서 S칸 이내의 최대 수익 출력
        print(max(dp[-1][-S:]))
    
    except:
        break