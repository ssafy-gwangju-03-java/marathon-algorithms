# N, S, T
# N: 출발점과 별 사이의 칸 수
#   (배열 길이)
# S: 1~S까지의 자연수가 주사위에 같은 확률로 나옴
#   (한 번에 이동가능한 최대 칸 수)
# T: T턴 후 게임 종료
#   (주사위 던질 수 있는 횟수)
# 테케 첫줄 이후로는 N 개의 정수가 주어짐.

while True:
    # 처음부터 N,S,T로 받으면 0들어올 때 ValueError ㅜㅜ
    NST = list(map(int, input().split()))
    if NST[0] == 0:
        break  # N == 0일 때 종료
    N, S, T = NST

    # 보드
    board = [0]  # start지점을 0으로 취급.
    # 보드 길이 N을 만족할 떄까지 입력 받아서 배열에 추가함.
    while len(board) <= N:  # 아하 앞에서 0을 넣고 시작했는데 while문 조건에 들어갈 board 길이를 하나 작게 해서 그런거였다!!!
        board.extend(list(map(int, input().split())))
    board += [0]
    '''
    board[0]
    while len(board) < N ~~~~~
    board += [0]
    이거랑 아래꺼랑 차이가 뭔데 런타임 에러가...????
    arr = []
    while len(arr) < N ~~~~~
    arr = [0] + arr + [0]
    '''
    # dp 배열 선언
    # dp[던진횟수][위치] = 해당 위치에서의 최대 값
    # 초기 값은 최대한 작은 값으로 설정 => 이후 최대 값 찾을 때 사용
    INF = 10000 * N * T
    dp = [[-INF] * (N + 2) for _ in range(T + 1)]

    # 첫 번째 주사위로 도달할 수 있는 위치값 설정
    # 시작 위치에서 주사위 눈의 값인 S까지의 값으로 초기 dp배열 초기화 (처음주사위로 갈수있는위치).
    dp[1][:S + 1] = board[:S + 1]

    # 각 시행에 대해 반복
    for stage in range(1, T):  # stage: 현재 던진 주사위 횟수
        # 각 위치에 대해 반복
        # 이전 단계에서 이미 stage-1 회차까지 계산한 값 기반으로 계산해서 여기서는 stage부터 시작
        for x in range(stage, N + 1):
            # 주사위 눈 수에 따라 이동가능한 각각의 위치에 대해 반복
            for step in range(1, S + 1):  # step: 주사위 던져서 나올 수 있는 눈의 수
                # 이동할 위치가 보드 끝 넘는경우
                if x + step > N:  # 보드 넘어가는 경우 처리하기 위한 조건. 이 경우는 보드 마지막 위치에 대해 최댓값 갱신함.
                    # 배열 끝 위치값 갱신
                    # 현재위치 x에서 stage번째 주사위 던지기 전까지의 최댓값(dp[stage][x]과 비교해서 큰 값 넣기
                    dp[stage + 1][-1] = max(dp[stage + 1][-1], dp[stage][x])
                else:
                    # 이동한 위치의 값 갱신
                    # 현재 위치 x에서 step만큼 이동한 위치인 `x + step`으로 가는 경우의 새로운 값과 비교해서 큰 값 넣기
                    dp[stage + 1][x + step] = max(dp[stage + 1][x + step], dp[stage][x] + board[x + step])
    # print('board', board)
    print(dp[-1][-1])
