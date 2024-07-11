import sys
from itertools import combinations

# 6개의 팀이 모든 팀과 한번씩 경기를 하는 경우의 수
# A = 0, B = 1, ..., F = 5
leagues = list(combinations(range(6), 2))

# 모든 경기 시마다 가능할 때 1씩 빼주며 결과의 참거짓 여부를 완전탐색
def play(results, round):
    global answer
    if round == 15:

        # 15번의 경기를 모두 마쳤을 때 가능한 경우라면 각 팀의 결과에 남아있는 숫자는 없어야 함
        for result in results:
            if result.count(0) != 3:
                return

        answer = 1
        return

    # player1, player2
    p1, p2 = leagues[round]

    # round1, round2
    # 각 튜플의 값은 승, 무, 패의 인덱스 값
    for r1, r2 in [(0, 2), (1, 1), (2, 0)]:

        # 각 팀의 승, 무, 패 값에서 셀 수 있는 경우의 수가 남아있다면 탐색
        if results[p1][r1] and results[p2][r2]:
            results[p1][r1] -= 1
            results[p2][r2] -= 1
            play(results, round + 1)
            results[p1][r1] += 1
            results[p2][r2] += 1


for _ in range(4):
    results = list(map(int, sys.stdin.readline().split()))
    results = [results[i:i + 3] for i in range(0, 16, 3)]
    answer = 0
    play(results, 0)
    print(answer, end=" ")
