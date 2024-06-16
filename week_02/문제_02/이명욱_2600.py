# 구슬게임
# 참고 https://ji-gwang.tistory.com/438, chatGPT
# 어렵다 dp dp 문제 좀 더 풀어야 할 듯 ㅜ
# 메모이제이션 : 동일한 계산의 반복 수행 제거

def win(p, q):
    # 이미 할당 된 값이 있으면 해당 결과를 반환
    if dp[p][q] >= 0:
        return dp[p][q]

    # p에 있는 구슬을 우선 빼기
    for i in range(3):
        # p에 있는 구슬을 뺄 수 있고 뺀 후에 구슬을 뺄 수 없다면
        if b[i] <= p and win(p - b[i], q) == 0:
            # 플레이어 승리 저장 후 반환
            dp[p][q] = 1
            return dp[p][q]

    # 그 후 q에 있는 구슬빼기
    for j in range(3):
        # q에 있는 구슬을 뺄 수 있고 뺀 후에 구슬을 뺄 수 없다면
        if b[j] <= q and win(p, q - b[j]) == 0:
            # 플레이어 승리 저장 후 반환
            dp[p][q] = 1
            return dp[p][q]

    # 구슬을 뺄 수 없다면 패배이기 때문에 결과 0 할당
    dp[p][q] = 0
    # 패배 반환
    return dp[p][q]


# dp[p][q] = 구슬이 한 통에는 p개, 다른 통에는 q개 있을 때 이길 수 있는지
dp = [[-1 for _ in range(501)] for _ in range(501)]
# 한 번에 뺄 수 있는 구슬의 개수 리스트
b = list(map(int, input().split()))
for _ in range(5):
    k1, k2 = map(int, input().split())
    if win(k1, k2):
        print("A")
    else:
        print("B")