import sys
sys.setrecursionlimit(10 ** 6)


class Egg:
    def __init__(self, durability, weight):
        self.durability = durability
        self.weight = weight

    def hit(self, another_egg):
        self.durability -= another_egg.weight
        another_egg.durability -= self.weight

    def recover(self, another_egg):
        self.durability += another_egg.weight
        another_egg.durability += self.weight

    def is_broken(self):
        return self.durability <= 0

    def __repr__(self):
        return f'[내구도: {self.durability}, 무게: {self.weight}]'


def dfs(curr, break_count):
    global answer

    if curr >= N:
        answer = max(answer, break_count)
        return

    did_hit = False
    for next in range(N):
        # 손에 들고 있는 계란이 깨지지 않은 경우 깨지지 않은 다른 계란 중에서 하나를 친다
        if next != curr and not egg_list[curr].is_broken() and not egg_list[next].is_broken():

            egg_list[curr].hit(egg_list[next])
            curr_count = int(egg_list[curr].is_broken()) + int(egg_list[next].is_broken())
            did_hit = True

            # 가장 최근에 든 계란의 한 칸 오른쪽 계란으로 이동
            dfs(curr + 1, break_count + curr_count)

            # 다른 계란을 깨는 경우의 수를 세줘야 하기 때문에 원상태로 복구해놓기
            egg_list[curr].recover(egg_list[next])

    # 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다
    if not did_hit:
        dfs(curr + 1, break_count)


N = int(sys.stdin.readline())
egg_list = []

for _ in range(N):
    durability, weight = map(int, sys.stdin.readline().split())
    egg_list.append(Egg(durability, weight))

answer = -1
dfs(0, 0)
print(answer)