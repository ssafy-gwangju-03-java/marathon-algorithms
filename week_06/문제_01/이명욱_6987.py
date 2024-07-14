# itertools : 효율적인 루핑을 위한 이터레이터를 만드는 함수

# itertools.combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합
# itertools.combinations_with_replacement(iterable, r) : iterable에서 원소 개수가 r개인 중복 조합
# itertools.permutations(iterable, r=None): iterable에서 원소 개수가 r개인 순열
# itertools.product(*iterable, repeat=1) : 여러 iterable의 데카르트곱 리턴
# ex) product(l1, l2, repeat=1) : l1과 l2의 모든 쌍을 지어 리턴
# ex) product(l1, repeat=3) = product(l1, l1, l1, repeat=1)


from itertools import combinations as cb

# 백트래킹
def solve(round):
    global ans
    # 15경기 종료 후 결과 확인하기
    if round == 15:
        ans = 1
        for sub in res:
            # 승무패 맞게 -1 되었으면 res 2차원 배열의 값이 모두 0
            if sub.count(0) != 3:
                ans = 0
                break
        return

    # 경기하는 두 개의 팀 뽑기
    t1, t2 = game[round]
    # (t1 승, t2 패), (t1 무, t2 무), (t1 패, t2 승) 비교하기
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1
            res[t2][y] -= 1
            solve(round + 1)
            res[t1][x] += 1
            res[t2][y] += 1


# 가능, 불가능 결과 넣을 리스트
answer = []
# 5개의 팀이 붙을 수 있는 조합 [(0, 1), (0, 2), (0, 3) ...]
game = list(cb(range(6), 2))
# print(game)

# 입력 받고 함수 실행
for _ in range(4):
    data = list(map(int, input().split()))
    # 한팀의 승, 무, 패 쪼개 넣기
    res = [data[i:i + 3] for i in range(0, 16, 3)]
    # print(res)
    ans = 0
    # 백트래킹 후 가능 불가능 결과 여부 어펜드
    solve(0)
    answer.append(ans)

print(*answer)