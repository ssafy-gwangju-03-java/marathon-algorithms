import sys
input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 좌표가 드래곤 커브에 포함이 되는지 체크해 줄 리스트
check = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    # 주어진 g세대 동안 움직인 방향을 담아둘 리스트
    move_list = [d]
    # 먼저 시작 하는 x,y 좌표는 방문 체크
    check[x][y] = 1
    # 세대 만큼 반복
    for i in range(g):
        tmp = []
        # 시작 세대 d로 초기화한 move_list의 길이만큼 반복
        for j in range(len(move_list)):
            # 이전 세대들을 순회하면서 뒤에서부터 방향에 1씩 더하고 4로 나누기
            tmp.append((move_list[-j - 1] + 1) % 4)
        # move_list에 extend
        move_list.extend(tmp)

    # move_list에 있는 방향을 확인하면서 좌표를 계산해주고, check 처리를 해준다.
    for i in move_list:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1
        # 방향 갱신
        x, y = nx, ny

answer = 0
# 기준, 오른쪽, 아래, 오른쪽 아래가 1로 체크 되어 있는지 확인
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
            answer += 1

print(answer)

# 참고 : https://resilient-923.tistory.com/350
# 직접 손으로 풀어보면서 규칙 찾기
# append != extend
# extend 리스트 더하기 리스트로 생각하기