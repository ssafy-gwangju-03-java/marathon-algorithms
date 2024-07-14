import sys

sys.stdin = open("../../input.txt", 'r')

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(4)]
teams = [i for i in range(6)]
select = [0] * 2
scores = [0] * 18
answer = [0] * 4

matches = []
# 6팀중 2팀 뽑기
def comb(idx, start):
    if idx == 2:
        matches.append(select[:])
        return

    for i in range(start, 6):
        select[idx] = teams[i]
        comb(idx + 1, i + 1)

comb(0, 0)

# 만들어진 matches로 경기진행
answer = [0] * 4

def play(round):
    global answer, scores

    if round == 15:
        for i, result in enumerate(arr):
            if scores == result:
                answer[i] = 1
        return

    n1, n2 = matches[round]


    # 1팀이 이기는 경우
    scores[n1 * 3] += 1
    scores[n2 * 3 + 2] += 1
    play(round + 1)
    scores[n1 * 3] -= 1
    scores[n2 * 3 + 2] -= 1

    # 무승부
    scores[n1 * 3 + 1] += 1
    scores[n2 * 3 + 1] += 1
    play(round + 1)
    scores[n1 * 3 + 1] -= 1
    scores[n2 * 3 + 1] -= 1

    # 2팀이 이기는 경우
    scores[n1 * 3 + 2] += 1
    scores[n2 * 3] += 1
    play(round + 1)
    scores[n1 * 3 + 2] -= 1
    scores[n2 * 3] -= 1

play(0)

print(*answer)
