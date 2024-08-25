# 공사 시작 전 N개 역, 공사 M번
N, M = map(int, input().split())
stations = list(map(int, input().split()))  # 공사 전 역들 고유 번호

# 양방향 연결 리스트 구현하자
next_station = {}  # 각 역의 다음 역 저장
prev_station = {}  # 각 역의 이전 역 저장

# 시작 전 역들을 연결 리스트로
for i in range(N):
    next_station[stations[i]] = stations[(i + 1) % N]
    prev_station[stations[i]] = stations[(i - 1) % N]

# 공사 M번 ㄱㄱ
for _ in range(M):
    command = input().split()

    if command[0] == 'BN':  # 다음 역 사이에 새 역 설립
        i, j = map(int, command[1:])
        print(next_station[i])  # 다음 역 번호 출력
        next_station[j] = next_station[i]  # 새 역의 다음 역 설정
        prev_station[next_station[i]] = j  # 기존 다음 역의 이전 역을 새 역으로 설정
        next_station[i] = j  # 현재 역의 다음 역을 새 역으로 설정
        prev_station[j] = i  # 새 역의 이전 역 설정

    elif command[0] == 'BP':  # 이전 역 사이에 새 역 설립
        i, j = map(int, command[1:])
        print(prev_station[i])  # 이전역 번호 출력
        prev_station[j] = prev_station[i]  # 새 역의 이전 역 설정
        next_station[prev_station[i]] = j  # 기존 이전 역의 다음 역을 새 역으로 설정
        prev_station[i] = j  # 현재 역의 이전 역을 새 역으로 설정
        next_station[j] = i  # 새 역의 다음 역 설정

    elif command[0] == 'CN':  # 다음 역 폐쇄
        i = int(command[1])
        closed = next_station[i]  # 폐쇄할 역 번호
        print(closed)  # 폐쇄되는 역 번호 출력
        next_station[i] = next_station[closed]  # 현재 역의 다음 역을 폐쇄 역의 다음 역으로 설정
        prev_station[next_station[closed]] = i  # 폐쇄 역의 다음 역의 이전 역을 현재 역으로 설정
        del next_station[closed]  # 폐쇄된 역 정보 삭제
        del prev_station[closed]

    elif command[0] == 'CP':  # 이전 역 폐쇄
        i = int(command[1])
        closed = prev_station[i]  # 폐쇄할 역 번호
        print(closed)  # 폐쇄되는 역 번호 출력
        prev_station[i] = prev_station[closed]  # 현재 역의 이전 역을 폐쇄 역의 이전 역으로 설정
        next_station[prev_station[closed]] = i  # 폐쇄 역의 이전 역의 다음 역을 현재 역으로 설정
        del next_station[closed]  # 폐쇄된 역 정보 삭제
        del prev_station[closed]