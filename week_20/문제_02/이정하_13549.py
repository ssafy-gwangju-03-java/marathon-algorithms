import heapq  # 우선순위 큐 써야겠다

# https://my-coding-notes.tistory.com/415
# 1. 입력- 시작점 n과 목표점 k
# 2. 방문 여부를 체크할 리스트 초기화
# 3. 우선순위 큐로 BFS 
# 4. 현재 위치에서 가능한 이동 방법 탐색 (순간이동, 앞으로 1칸, 뒤로 1칸)
# 5. 목적지 도착하면 소요 시간 출력 및 종료

n, k = map(int, input().split())  # 시작점 n, 목적지 k
visited = [False] * 100001
visited[n] = True  # 시작점 방문 처리
hq = [([0, n])]  # 우선순위 큐 초기화: [시간, 위치]

while hq:  # 큐가 비어있지 않은 동안 반복
    t, x = heapq.heappop(hq)  # 현재 시간, 위치
    if x == k:  # 목적지 도착했으면
        print(t)  # 소요 시간 출력
        break

    # 순간이동 처리 (2*X)
    dx = x * 2
    if dx < len(visited) and not visited[dx]:  # 범위 내이고 미방문이면
        visited[dx] = True  # 방문 처리
        heapq.heappush(hq, (t, dx))  # 큐에 추가 (시간 증가 없음)

    # 걷기 처리 (X+1, X-1)
    for i in (x + 1, x - 1):
        if 0 <= i < len(visited) and not visited[i]:  # 범위 내이고 미방문이면
            visited[i] = True  # 방문 처리
            heapq.heappush(hq, (t + 1, i))  # 큐에 추가 (시간 1 증가)
