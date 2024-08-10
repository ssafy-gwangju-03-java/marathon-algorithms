import sys

N, K = map(int, sys.stdin.readline().split())

"""
can_go = {
    샘 좌표 1: [왼쪽에 집 짓기 가능여부, 오른쪽에 집짓기 가능 여부],
    샘 좌표 2: ...,
    ...
}
"""

can_go = {}
for saem in list(map(int, sys.stdin.readline().split())):
    can_go[saem] = [True, True]

built = set()   # 지은 집들
unhappiness = 0 # 불행도
dist = 1        # 샘으로부터 거리

def build_house(next_house, saem, dir):
    global unhappiness

    # 만약 집을 지으려는 좌표에 이미 집이나 샘이 존재하면 해당 방향으로 더이상 탐색할 수 없다
    if next_house in built or next_house in can_go:
        can_go[saem][dir] = False
    else:
        built.add(next_house)
        unhappiness += dist


while len(built) < K:
    to_remove = []

    # 각 샘마다 좌, 우를 탐색하며 가까운 곳부터 집을 지어준다
    for saem in can_go.keys():
        left, right = can_go[saem]

        # 만약 해당 샘이 더이상 탐색 불가능 하다면 삭제 예정 목록에 더해준다
        if not left and not right:
            to_remove.append(saem)
            continue

        if left:
            build_house(saem - dist, saem, 0)
            if len(built) == K:
                break

        if right:
            build_house(saem + dist, saem, 1)
            if len(built) == K:
                break

    # 더이상 탐색이 불가능한 샘들은 순회 목록에서 삭제한다
    for saem in to_remove:
        can_go.pop(saem)

    # 순회 후 거리는 1씩 증가
    dist += 1


print(unhappiness)