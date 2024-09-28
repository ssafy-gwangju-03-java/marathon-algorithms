N, M = map(int, input().split())
lst = list(map(int, input().split()))
prev = [0] * 1000001
next = [0] * 1000001
ans = []

for i in range(N):
    prev[lst[i]] = lst[i - 1]
    next[lst[i - 1]] = lst[i]

for _ in range(M):
    line = list(map(str, input().split()))
    if line[0] == "BN":
        i, j = int(line[1]), int(line[2])
        ans.append(next[i])
        nxt = next[i]
        next[j] = nxt
        prev[j] = i
        next[i] = j
        prev[nxt] = j
    elif line[0] == "BP":
        i, j = int(line[1]), int(line[2])
        ans.append(prev[i])
        prv = prev[i]
        next[j] = i
        prev[j] = prv
        next[prv] = j
        prev[i] = j
    elif line[0] == "CN":
        i = int(line[1])
        ans.append(next[i])
        nxt = next[i]
        nnxt = next[nxt]
        next[i] = nnxt
        prev[nnxt] = i
    else:
        i = int(line[1])
        ans.append(prev[i])
        prv = prev[i]
        pprv = prev[prv]
        next[pprv] = i
        prev[i] = pprv

for i in ans:
    print(i)


# 시간초과 풀이 - 객체로 하니까 초과
# import sys
# input = sys.stdin.readline
#
#
# class Node:
#     def __init__(self, prev, curr, nxt):
#         self.prev = prev
#         self.curr = curr
#         self.nxt = nxt
#
#     def __repr__(self):
#         return f'{self.prev} {self.curr} {self.nxt}'
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
#
# nodes = [0] * 1_000_001
# for i in range(N):
#     curr = arr[i]
#     nxt = arr[(i+1) % N]
#     prev = arr[(i-1) % N]
#     nodes[curr] = Node(prev, curr, nxt)
#
# for _ in range(M):
#     command = input().split()
#     i = int(command[1])
#
#     if command[0] == "BN":
#         j = int(command[2])
#         curr_node = nodes[i]
#         nxt_node = nodes[curr_node.nxt]
#         print(curr_node.nxt)
#
#         new_node = Node(curr_node.curr, j, nxt_node.curr)
#         curr_node.nxt = j
#         nxt_node.prev = j
#
#         nodes[j] = new_node
#
#     elif command[0] == "BP":
#         j = int(command[2])
#
#         curr_node = nodes[i]
#         prev_node = nodes[curr_node.prev]
#         print(curr_node.prev)
#
#         new_node = Node(prev_node.curr, j, curr_node.curr)
#         curr_node.prev = j
#         prev_node.nxt = j
#
#         nodes[j] = new_node
#
#     elif command[0] == "CP":
#         curr_node = nodes[i]
#         prev_node = nodes[curr_node.prev]
#         print(curr_node.prev)
#         prevprev_node = nodes[prev_node.prev]
#         nodes[curr_node.prev] = 0
#
#         curr_node.prev = prevprev_node.curr
#         prevprev_node.nxt = curr_node.curr
#
#
#     elif command[0] == "CN":
#         curr_node = nodes[i]
#         nxt_node = nodes[curr_node.nxt]
#         print(curr_node.nxt)
#         nxtnxt_node = nodes[nxt_node.nxt]
#         nodes[curr_node.nxt] = 0
#
#         curr_node.nxt = nxtnxt_node.curr
#         nxtnxt_node.prev = curr_node.curr


