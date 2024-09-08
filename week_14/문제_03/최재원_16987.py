import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("../../input.txt")

input = sys.stdin.readline


class Egg:
    def __init__(self, durability, weight):
        self.durability = durability
        self.weight = weight

    def __repr__(self):
        return f'egg({self.durability}, {self.weight})'

    def hit(self, opponent):
        self.durability -= opponent.weight

    def is_broken(self):
        return self.durability <= 0

    def roll_back(self, opponent):
        self.durability += opponent.weight


N = int(input())
eggs = []

for _ in range(N):
    eggs.append(Egg(*map(int, input().split())))

max_v = 0


# 계란을 하나씩 들어 치기
def dfs(idx, broken_eggs_count):
    global max_v

    if idx == N:
        max_v = max(max_v, broken_eggs_count)
        return

    # 남은 안깨진 계란의 수와 현재까지 깨진 계란을 합친게 max_v보다 작으면 취소
    remain_count = 0
    for egg in eggs:
        if not egg.is_broken():
            remain_count += 1

    if broken_eggs_count + remain_count <= max_v:
        return

    # 계란 하나씩 깨기
    hit = False
    for i in range(N):
        hit_count = 0

        # 들고있는 계란 선택 안함, 칠 계란이 안깨졌고, 들고있는 계란이 안깨졌으면
        if i != idx and not eggs[i].is_broken() and not eggs[idx].is_broken():
            eggs[i].hit(eggs[idx])
            eggs[idx].hit(eggs[i])

            if eggs[i].is_broken():
                hit_count += 1
            if eggs[idx].is_broken():
                hit_count += 1

            hit = True

            dfs(idx + 1, broken_eggs_count + hit_count)

            # 계란 복구
            eggs[i].roll_back(eggs[idx])
            eggs[idx].roll_back(eggs[i])

    if not hit:
        dfs(idx + 1, broken_eggs_count)


dfs(0, 0)
print(max_v)
