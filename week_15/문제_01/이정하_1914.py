# 하노이의 탑

# 하노이탑 함수
def hanoi(n, s, e, sub):
    """
    하노이탑 재귀
    :param n: 옮길 원판 개수
    :param s: 시작하는 기둥
    :param e: 도착할 기둥
    :param sub: 보조로 쓸 기둥
    """
    global cnt

    if n == 1:
        # 원판이 하나면 직접 옮긴다
        # moves.append((s, e))
        # cnt += 1
        print(s, e)
    else:
        # 1. n-1개를 sub 기둥으로 옮기기
        hanoi(n - 1, s, sub, e)
        # 2. 남은 가장 큰 원판을 도착 기둥으로 옮기기
        # moves.append((s, e))
        # cnt += 1  # 이동횟수 ++
        print(s, e)
        # 3. sub 기둥에 있는 n-1개를 도착 기둥으로 옮기기
        hanoi(n - 1, sub, e, s)


# 원판개수 N
N = int(input())

# 옮긴 횟수
# cnt = 0
# 이동과정 - A번 탑 -> B번 탑 = A B
moves = []

# 하노이 탑 시작
# 원팬 N개를 1번에서 3번으로, 보조는 2번
# hanoi(N, 1, 3, 2)  # 모든 경우에 전부 다 계산해버리니까 시간초과....

# 옮긴 횟수는 2^N -1
# => 미리 출력해놓고 N <20 에서만 추가로 출력 ㄱㄱ
'''
f(N-1) + 1 + f(N-1) = 원판 N개일 때 = 2*f(N-1) + 1
f(N) = 2 * f(N-1) + 1, f(1) = 1 = 2^1 - 1
f(2) = 2 * f(1) + 1 = 2*1 + 1 = 3 = 2^2 - 1
f(3) = 2 * f(2) + 1 = 2*3 + 1 = 7 = 2^3 - 1
f(4) = 2 * f(3) + 1 = 2*7b + 1 = 15 = 2^4 - 1
f(N = 2^N - 1
'''
print(2 ** N - 1)  # 옮긴횟수 먼저 따로 출력

if N <= 20:  # 20 이하일때만 과정 계산
    # for move in moves:
    #     print(move[0], move[1])
    hanoi(N, 1, 3, 2)
