def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n - 1, start, 6 - start - end)
    print(start, end)
    hanoi_tower(n - 1, 6 - start - end, end)


n = int(input())
# 횟수 출력
print(2 ** n - 1)
# n이 20보다 작거나 같을때 만 과정 출력
if n <= 20:
    hanoi_tower(n, 1, 3)