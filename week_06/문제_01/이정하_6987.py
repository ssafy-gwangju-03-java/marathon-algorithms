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
'''