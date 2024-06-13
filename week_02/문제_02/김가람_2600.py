
# b[0], b[1], b[2] == 한 번에 꺼낼 수 있는 구슬의 수 b1, b2, b3
b = list(map(int, input().split()))

# 한 통에 들어있는 구슬 수의 최대 갯수 500개
# 경우의 수 : 500 * 500
# 행, 열 : k1, k2
# 값 : A의 승리 여부
memo = [[False] * 501 for _ in range(501)]

for i in range(501):
    for j in range(501):
        # 구슬 통에서 b[k]개 꺼내기 전의 결과가 패배일 때, b[k]개가 더 있다면 내가 (A가) 꺼낼 수 있으니까 승리
        # 꺼낼 구슬이 없다면 패배이므로 memo[0][0]는 False

        # k1개 들어있는 통에서 구슬 꺼내기
        for k in range(3):
            if i-b[k] >= 0 and not memo[i-b[k]][j]:
                memo[i][j] = True
                break

        # k2개 들어있는 통에서 구슬 꺼내기
        for k in range(3):
            if j-b[k] >= 0 and not memo[i][j-b[k]]:
                memo[i][j] = True
                break

for _ in range(5):
    p, q = map(int, input().split())
    print("A" if memo[p][q] else "B")