n, h = map(int, input().split())
lst = [0 for _ in range(h)] 

for i in range(n):
    x = int(input())
    if i % 2 == 0:
        lst[h - x] += 1
    else:
        lst[0] += 1
        lst[x] -= 1
# print(lst)

prefix = [0 for _ in range(h + 1)] # 누적합 리스트
for i in range(h):
    prefix[i + 1] = prefix[i] + lst[i]

prefix.sort()
print(prefix[1], end=" ")
if prefix[1] == 0:
    print(prefix.count(0) - 1)
else:
    print(prefix.count(prefix[1]))
