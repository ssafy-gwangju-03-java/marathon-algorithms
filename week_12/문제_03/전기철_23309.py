# 23309 철도 공사

n, m = map(int, input().split())
lst = list(map(int, input().split()))
prev = [0] * 1000001  # 이전 역 저장할 리스트
next = [0] * 1000001  # 다음 역 저장할 리스트
ans = []
for i in range(n):
    prev[lst[i]] = lst[i - 1]
    next[lst[i - 1]] = lst[i]
for _ in range(m):
    line = list(map(str, input().split()))
    if line[0] == "BN":
        i, j = int(line[1]), int(line[2])
        ans.append(next[i])
        nxt = next[i]  # i j nxt 기준 잡고 연결라인 재설정
        next[j] = nxt
        prev[j] = i
        next[i] = j
        prev[nxt] = j
    elif line[0] == "BP":
        i, j = int(line[1]), int(line[2])
        ans.append(prev[i])
        prv = prev[i]  # j prv i 기준 잡고 연결라인 재설정
        next[j] = i
        prev[j] = prv
        next[prv] = j
        prev[i] = j
    elif line[0] == "CN":
        i = int(line[1])
        ans.append(next[i])
        nxt = next[i]
        nnxt = next[nxt]  # i nxt nnxt에서 nxt를 제거하고 i와 nnxt 연결
        next[i] = nnxt
        prev[nnxt] = i
    else:
        i = int(line[1])
        ans.append(prev[i])
        prv = prev[i]
        pprv = prev[prv]  # pprv prv i에서 prv 제거하고 pprv와 i 연결
        next[pprv] = i
        prev[i] = pprv
for i in ans:
    print(i)
