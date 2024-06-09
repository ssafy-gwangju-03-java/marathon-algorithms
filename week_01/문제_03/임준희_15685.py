n = int(input()) 
graph = [[0] * 101 for _ in range(101)]  # 101x101로 초기화
dx = [0, -1, 0, 1]  
dy = [1, 0, -1, 0]  

for i in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1  # 시작점을 1로 설정

    # 드래곤 커브 방향 리스트 초기화
    curve = [d]
    for j in range(g):  # g 세대까지 
        # 이전 세대의 반대 방향부터 역순으로 돌면서 새로운 방향 추가
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)
    
    # 드래곤 커브 표시
    for d in curve:
        x += dx[d]
        y += dy[d]
        if 0 <= x < 101 and 0 <= y < 101:
            graph[x][y] = 1

result = 0
# 모든 1x1 정사각형 순회하면서 꼭지점이 모두 1인지 확인
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            result += 1

print(result) 