# 23309번 철도 공사
# 구현, 연결리스트
# 접근 방법:
# 인덱스 = 역의 고유 번호
# 거기에 저장된 값 = (이전역, 다음역)

import sys
# pypy 에서 실행 가능
import os, io, __pypy__

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()


def main():
    N, M = map(int, input().split())
    station_list = list(map(int, input().split()))

    prv = [0 for _ in range(1_000_000 + 1)]
    nxt = [0 for _ in range(1_000_000 + 1)]

    for i in range(N):
        now_station_num = station_list[i]
        prv[now_station_num] = station_list[i - 1]
        nxt[now_station_num] = station_list[(i + 1) % N]

    # A > B > C to A > B > D > C
    def insert(B, D):
        C = nxt[B]
        nxt[B] = D
        prv[D], nxt[D] = B, C
        prv[C] = D

    # A > B > C to A > C
    def remove(B):
        A, C = prv[B], nxt[B]
        nxt[A], prv[C] = C, A

    for _ in range(M):
        information = input().split()
        command = information[0]
        if command == b'BN':
            i, j = int(information[1]), int(information[2])
            ans.append(str(nxt[i]) + '\n')
            insert(i, j)
        elif command == b'BP':
            i, j = int(information[1]), int(information[2])
            ans.append(str(prv[i]) + '\n')
            insert(prv[i], j)
        elif command == b'CN':
            i = int(information[1])
            ans.append(str(nxt[i]) + '\n')
            remove(nxt[i])
        else:
            i = int(information[1])
            ans.append(str(prv[i]) + '\n')
            remove(prv[i])

    os.write(1, ans.build().encode())


if __name__ == '__main__':
    main()