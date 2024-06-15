# k1에 남은 구슬 개수, k2에 남은 구슬 개수, 현재 누구 차례인지, dp배열
def solve(remain_k1, remain_k2, turn, dp):
    # 이미 계산된 적 있으면 해당 결과 (플레이어 1 or -1) 리턴
    if dp[remain_k1][remain_k2] != 0:
        return dp[remain_k1][remain_k2]

    # B 승리(A 패배)로 초기화
    # check = -1

    # 이제 세 가지 구슬 뺄 수 있는 경우에 대해 반복
    for now_b in b:
        # 현재 차례인 사람이 k1에서 now_b만큼 구슬 꺼낼 수 있는 경우
        if now_b <= remain_k1:
            # 상대방이 패배하는 경우가 있으면
            if solve(remain_k1 - now_b, remain_k2, -turn, dp) == -1:
                dp[remain_k1][remain_k2] = 1  # 현재 플레이어 승리할 수 있음!
                return 1

        # 현재 차례인 사람이 k2에서 now_b만큼 구슬 꺼낼 수 있는 경우
        if now_b <= remain_k2:
            # 상대방이 패배하는 경우가 있으면
            if solve(remain_k1, remain_k2 - now_b, -turn, dp) == -1:
                dp[remain_k1][remain_k2] = 1  # 현재 플레이어가 승리
                return 1

    # 상대방이 모두 승리하는 경우 여기까지 옴
    # 그러면 현재 플레이어는 패배
    dp[remain_k1][remain_k2] = -1
    return -1


# 꺼낼수있는 구슬 개수 b1, b2, b3
b = list(map(int, input().split()))

for _ in range(5):
    k1, k2 = map(int, input().split())
    # dp[p][q] = k1에 p개, k2에 q개 구슬 남아있을 때 1이면 A가 승, -1이면 B가 승
    dp = [[0 for _ in range(500 + 1)] for _ in range(500 + 1)]  # r(501) 여부는 이따 생각해보자.. (k1,k2범위가 1~500)
    # 이제 구슬게임 시작!
    # solve 함수로 재귀쓸거라서 함수 필요함
    winner = solve(k1, k2, 1, dp)  # A는 1, B는 -1. A부터 시작.
    # results = []
    if winner == 1:
        print('A')
    elif winner == -1:
        # results.append('B')
        print('B')
