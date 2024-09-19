from collections import defaultdict

# N*N 격자, 파이어볼 M개, 이동명령 K번
N, M, K = map(int, input().split())

# 파이어볼 정보
fireball_info = [list(map(int, input().split())) for _ in range(M)]
# fi[i][0], fi[i][1] : i번 파이어볼의 위치 (r,c)
# fi[i][2] = m (파이어볼 질량) ☆
# fi[i][3] = s (속력-s개의 칸)
# fi[i][4] = d (방향)

# 델타 배열
# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# N*N 격자
arr = [[0] * N for _ in range(N)]
# print(arr)
# 이동 명령 K번
for order in range(K):
    # 각 위치에 있는 파이어볼 정보를 저장할 딕셔너리
    fireballs = defaultdict(list)

    # 매 명령마다 모든 파이어볼 이동
    for r, c, m, s, d in fireball_info:
        # 이건 왜 이렇게 되는거지,,
        # nr = (r - 1 + dr[d] * s) % N + 1
        # nc = (c - 1 + dc[d] * s) % N + 1
        nr, nc = r + dr[d] * (s % N), c + dc[d] * (s % N)  # 각 행,열의 1번과 N번은 연결되어있음
        # 격자 범위 벗어나면 (한가운데에서 N-1칸 가거나 하는 식으로)
        if nr < 0 or nr >= N:
            nr = nr - N if nr >= N else nr + N
        if nc < 0 or nc >= N:
            nc = nc - N if nc >= N else nc + N

        # if (nr, nc) not in fireballs:
        fireballs[(nr, nc)].append([m, s, d]) # 새 위치에 파이어볼 정보 저장
        # print(fireballs)

    # 새로운 파이어볼 정보 배열
    # new_fb_info = defaultdict(list)
    new_fb_info = []  # new_fb_info is simply a collection of fireball information that gets updated and isn't really dependent on being keyed by coordinates

    # 각 위치에서 파이어볼 처리
    for (r, c), fbs in fireballs.items():
        # print(r,c,fbs)
        # print(len(fbs))
        if len(fbs) == 1:
            # 파이어볼 한 개면 그대로 추가
            new_fb_info.append([r, c] + fbs[0])
        elif len(fbs) > 1:# 파이어볼 두 개 이상이면 ?
            total_m, total_s, cnt, all_even_odd = 0, 0, len(fbs), True
            for m, s, d in fbs: # 질량, 속략 합하고
                total_m += m
                total_s += s
                if all_even_odd and cnt > 1:
                    # 방향 홀짝 일치 여부
                    all_even_odd = (fbs[0][2] % 2 == d % 2)

            new_m = total_m // 5 # 새 질량 계산하자

            if new_m > 0:  # 질량 0인 파이어볼은 소멸, 속력/방향 계산
                new_s = total_s // cnt
                new_d = [0, 2, 4, 6] if all_even_odd else [1, 3, 5, 7]
                for d in new_d:
                    # 새 파이어볼 저장
                    new_fb_info.append([r, c, new_m, new_s, d])
    fireball_info = new_fb_info

# 남아있는 파이어볼 질량의 합 계산
result = sum(fb[2] for fb in fireball_info)
print(result)
