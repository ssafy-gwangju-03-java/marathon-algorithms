from itertools import combinations


def dfs(idx):
    global ans
    # 1. 종료조건 - 마지막 (15번쨰)경기에 도달하면
    if idx == 15:
        # 모든 승-무-패
        for i in group:
            if sum(i) != 0:
                return  # 다 뺐으니까 0이어야되는데 , 0이 아니면 불가능한 결과
        ans = 1
        return

    # 이번 매치에 참여할 팀 정보를 가져오자
    t1, t2 = games[idx][0], games[idx][1]

    # 가능한 경우를 순회 - 승-패, 무-무, 패-승
    for one, two in ((0, 2), (1, 1), (2, 0)):
        # 가능한 범위라면
        if group[t1][one] > 0 and group[t2][two] > 0:
            # 깎아버리자
            group[t1][one] -= 1
            group[t2][two] -= 1
            dfs(idx + 1)
            # 복구하고 다음걸로
            group[t1][one] += 1
            group[t2][two] += 1


answer = []
for _ in range(4):
    ans = 0
    result = list(map(int, input().split()))
    group = []

    # 각 팀별로 승-무-패 구분해서 넣어둘 것이다
    for i in range(0, 18, 3):
        group.append([result[i], result[i + 1], result[i + 2]])

    # 가능한 모든 조합
    games = list(combinations(range(6), 2))

    dfs(0)  # 첫 번째 매치부터 시작하자

    # 이번 경우의 답 저장하기
    answer.append(ans)
print(*answer)

"""
def dfs(tc, cur_match):
    # 1.종료조건 - 경기 15개 모두 탐색 완료
    if cur_match == 15:
        if answer[tc]:  # 이미 가능한 경우로 판단되었으면 탐색 종료
            return
        # 주어진 예상 결과와 내가 계산한 결과가 일치하는지 chk
        for r in range(6):
            for c in range(3):
                if group[r][c] != result[r][c]:
                    return
        # else:  # 모든 결과가 같았으면 결과에 가능 표기
        answer[tc] = 1
        # print('yes')
        return




    # 2. 탐색
    # 현재 경기중인 팀의 idx
    t1 = team1[cur_match]
    t2 = team2[cur_match]

    # t1 vs t2
    # (1) 승-패
    result[t1][0] += 1  # 팀1 승
    result[t2][2] += 1  # 팀2 패
    dfs(tc, cur_match + 1)  # 이 경우 다음 것 탐색하기
    # 무-무 탐색 전 복구
    result[t1][0] -= 1
    result[t2][2] -= 1

    # (2) 무-무
    result[t1][1] += 1
    result[t2][1] += 1
    dfs(tc, cur_match + 1)
    result[t1][1] -= 1
    result[t2][1] -= 1

    # (3) 패-승
    result[t2][0] += 1  # 팀2 승
    result[t1][2] += 1  # 팀1 패
    dfs(tc, cur_match + 1)  # 이 경우 다음 것 탐색하기
    # 탐색 후 복구
    result[t2][0] -= 1
    result[t1][2] -= 1


league = [list(map(int, input().split())) for _ in range(4)]

# print(league)

answer = [0] * 4  # 가능한 결과인지 여부 0,1
# 팀 0번 ~ 5번까지의 조합
team1 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
team2 = [1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5]

for tc in range(4):
    # 초기화 위치!!!!!
    group = [[0] * 3 for _ in range(6)]  # 입력으로 주어진 하나의 리그를 3*6 형태로 다시 저장
    result = [[0] * 3 for _ in range(6)]  # 탐색과정 중 경기 결과 저장
    idx = 0
    for r in range(6):
        # print(r)
        for c in range(3):
            # print('c:',c)
            # print('(',r,c,')', 'idx: ', idx)
            group[r][c] = league[tc][idx]
            # print(league[tc][idx])
            idx += 1
    dfs(tc, 0)  # 테케번호, 몇라운드인지
    # print('tc',tc)
print(*answer)
# print('group', group)"""
"""
# 승 무 패 * 6개국 *  4개 조

league = [list(map(int, input().split())) for _ in range(4)]
result = [1] * 4
for tc in range(4):
    if sum(league[tc]) != 30:  # 합이 30이 아니면 불가능
        result[tc] = 0
        continue
    # 승 - 패 각각의 합이 같지 않으면 return 0
    if sum(league[tc][i] for i in range(0, 18, 3)) != sum(league[tc][i] for i in range(2, 18, 3)):
        result[tc] = 0
        continue
    # 무승부 합 %2 가 0이 아니면 return 0
    if sum(league[tc][i] for i in range(1, 18, 3)) % 2 != 0:
        result[tc] = 0
        continue
    cnt = 0
    for i in range(1, 18, 3):
        if league[tc][i]:
            cnt += 1
    # 무승부가 나온 팀 개수가 홀수개면 return 0
    # if cnt % 2 == 0: => 홀수개여도 가능 - 1개보다 크면
    # 무승부가 나온 팀 개수가 1개면 return 0
    if cnt == 1:
        result[tc] = 0
        continue
print(' '.join(map(str, result)))
'''
전부 1
'''
'''
500
401
302
113
014
023
'''
'''
5 0 0 4 0 1 2 0 3 1 1 3 0 1 4 2 0 3
5 0 0 4 0 1 2 0 3 0 1 4 1 1 3 1 2 2
5 0 0 4 0 1 2 1 2 2 0 3 1 1 3 0 0 5
5 0 0 4 0 1 2 1 2 2 0 3 0 2 3 0 1 4
5 0 0 4 0 1 2 1 2 2 0 3 0 1 4 1 0 4
5 0 0 4 0 1 2 1 2 1 1 3 0 1 4 1 1 3
5 0 0 4 0 1 2 1 2 1 0 4 1 1 3 1 0 4
5 0 0 4 0 1 2 1 2 1 0 4 0 2 3 1 1 3
5 0 0 4 0 1 2 1 2 1 0 4 0 1 4 2 0 3
5 0 0 4 0 1 2 1 2 1 1 3 0 2 3 1 0 4
5 0 0 4 0 1 2 1 2 0 2 3 0 2 3 1 1 3
'''
'''
3 0 2 3 0 2 3 0 2 2 0 3 2 0 3 2 0 3
3 0 2 3 0 2 3 0 2 2 0 3 2 0 3 2 0 3
3 0 2 3 0 2 3 0 2 2 0 3 2 0 3 2 0 3
3 0 2 3 0 2 3 0 2 2 0 3 2 0 3 2 0 3
'''
'''
5 0 0 5 0 0 5 0 0 0 0 5 0 0 5 0 0 5
5 0 0 4 0 1 4 0 1 1 0 4 1 0 4 0 0 5
0 5 0 5 0 0 0 0 5 0 5 0 0 5 0 0 5 0
0 5 0 0 5 0 3 0 2 2 0 3 4 0 1 1 0 4
'''"""
