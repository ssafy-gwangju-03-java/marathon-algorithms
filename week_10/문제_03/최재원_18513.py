import sys
from collections import deque

sys.stdin = open("../../input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
sam = list(map(int, input().split()))


def build_house(curr, next):
    global house_count, unhappiness

    # 다음 집의 불행도는 현재 집 + 1
    dic[next] = dic[curr] + 1
    house_count += 1

    # 불행도 누적
    unhappiness += dic[next]

    # 집 개수를 다 채우면 불행도 출력 후 종료
    if house_count == K:
        print(unhappiness)
        exit()

    # 큐에 다음 집 넣기
    q.append(next)


def bfs():

    while q:
        curr = q.popleft()
        right = curr + 1
        left = curr - 1

        # 딕셔너리에 집이 없으면 집 추가
        if right not in dic.keys():
            build_house(curr, right)

        if left not in dic.keys():
            build_house(curr, left)


# 집을 짓고 불행도를 저장할 딕셔너리
dic = {}
q = deque()

# 샘물의 불행도는 0, 큐에 샘물 넣고 BFS 시작
for p in sam:
    dic[p] = 0
    q.append(p)

house_count = 0
unhappiness = 0

bfs()
