# https://www.acmicpc.net/problem/23309

## Referenced
# https://developerjisu.tistory.com/18

import sys

input = sys.stdin.readline


def BN(i, j):
    """
    현재 i 역과 그 다음 역 사이에 j 역 생성 후 다음 역 번호 반환
    """
    i, j = int(i), int(j)
    post_station = post_info[i]
    post_info[i] = j
    prev_info[j] = i
    post_info[j] = post_station
    prev_info[post_station] = j
    return post_station


def BP(i, j):
    """
    현재 i 역과 그 이전 역 사이에 j 역 생성 후 이전 역 번호 반환
    """
    i, j = int(i), int(j)
    prev_station = prev_info[i]
    prev_info[i] = j
    post_info[j] = i
    prev_info[j] = prev_station
    post_info[prev_station] = j
    return prev_station


def CN(i):
    """
    현재 i 역의 그 다음 역을 폐쇄 후 폐쇄된 역 번호 반환
    """
    i = int(i)
    station_to_close = post_info[i]
    post_station = post_info[station_to_close]
    post_info[i] = post_station
    prev_info[post_station] = i
    return station_to_close


def CP(i):
    """
    현재 i 역의 그 이전 역을 폐쇄 후 폐쇄된 역 번호 반환
    """
    i = int(i)
    station_to_close = prev_info[i]
    prev_station = prev_info[station_to_close]
    prev_info[i] = prev_station
    post_info[prev_station] = i
    return station_to_close


N, M = map(int, input().split())
stations = list(map(int, input().split()))

# 인덱스를 역의 고유번호로 하는 앞, 뒤 역 정보 저장 배열
prev_info = [0] * 1000001
post_info = [0] * 1000001

# 역 정보 배열 초기화
first_station = stations[0]
prev_station = first_station

for station in stations[1:-1]:
    prev_info[station] = prev_station
    post_info[prev_station] = station
    prev_station = station

last_station = stations[-1]
post_info[prev_station] = last_station
prev_info[last_station] = prev_station
post_info[last_station] = first_station
prev_info[first_station] = last_station

result = []
for _ in range(M):
    cmd_input = iter(input().split())
    cmd = next(cmd_input)

    if cmd == "BN":
        result.append(BN(next(cmd_input), next(cmd_input)))
    elif cmd == "BP":
        result.append(BP(next(cmd_input), next(cmd_input)))
    elif cmd == "CP":
        result.append(CP(next(cmd_input)))
    elif cmd == "CN":
        result.append(CN(next(cmd_input)))

print(*result, sep="\n")
