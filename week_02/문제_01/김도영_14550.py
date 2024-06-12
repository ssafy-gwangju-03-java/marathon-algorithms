# # 마리오 파티

# from collections import deque

# # N : 출발점과 별 사이의 칸 수
# # S : 1부터 S까지의 자연수
# # T : 턴 수
# N, S, T = map(int, input().split())

# while True:
#     try:
#         board = []
        
#         while len(board) != N:
#             board = board + list(map(int, input().split()))

#         dp = [-1e9] * N

#         # 첫 번째 턴
#         for i in range(min(S, N)):
#             dp[i] = board[i]

#         print(dp)
#         # 두 번째 턴 이후
#         for _ in range(1, T):
#             new_dp = [-1e9] * N

#             for i in range(N):
#                 if dp[i] != -1e9:
#                     for s in range(1, S + 1):
#                         if i + s < N:
#                             new_dp[i + s] = max(new_dp[i + s], dp[i] + board[i + s])
            
#             dp = new_dp

#             print(dp)
        
#         print(max(dp[:N]))

#         N, S, T = map(int, input().split())

#     # 예외 처리를 통해 반복문 빠져나가기
#     except ValueError:
#         break

from collections import deque

# N : 출발점과 별 사이의 칸 수
# S : 1부터 S까지의 자연수
# T : 턴 수
N, S, T = map(int, input().split())

while True:
    try:
        board = []
        
        while len(board) != N:
            board = board + list(map(int, input().split()))

        dp = [-1e9] * (N + 1)

        # 첫 번째 턴
        for i in range(S):
            if i < N:
                dp[i] = board[i]

        # print(dp)

        # 두 번째 턴 이후
        for _ in range(1, T - 1):
            new_dp = [-1e9] * N

            for i in range(N):
                if dp[i] != -1e9:
                    for s in range(1, S + 1):
                        if i + s < N:
                            new_dp[i + s] = max(new_dp[i + s], dp[i] + board[i + s])
            
            dp = new_dp
            # print(dp)
        
        # 결과 출력
        print(max(dp[N - S:]))

        # 다음 입력 받기
        N, S, T = map(int, input().split())

    # 예외 처리를 통해 반복문 빠져나가기
    except ValueError:
        break
