# 1. 입력 - 전구 개수 N, 초기 상태, 목표 상태
# 2. 첫 번째 전구를 누르지 않은 경우 시뮬레이션
# 3. 첫 번째 전구를 누른 경우 시뮬레이션
# 4. 두 경우 중 성공한 경우의 스위치 조작 횟수 출력
# 5. 둘 다 실패한 경우 -1 출력

N = int(input())  # 전구 개수

before = list(map(int, input()))  # 초기 상태
after = list(map(int, input()))  # 목표 상태
temp_before = before[:]  # 초기 상태 복사
cnt = 0  # 스위치 조작 횟수

# 첫 번째 전구를 누르지 않은 경우
for i in range(1, N):
    if before[i - 1] != after[i - 1]:  # 이전 전구 상태가 다르면
        cnt += 1  # 스위치 조작 횟수 증가
        before[i] = int(not before[i])  # 현재 전구 상태 변경
        before[i - 1] = int(not before[i - 1])  # 이전 전구 상태 변경
        if i != N - 1:
            before[i + 1] = int(not before[i + 1])  # 다음 전구 상태 변경
else:
    if ''.join(map(str, before)) == ''.join(map(str, after)):  # 목표 상태와 일치하면
        print(cnt)  # 조작 횟수 출력
        exit()  # 프로그램 종료

# 첫 번째 전구를 누른 경우
cnt = 1  # 스위치 조작 횟수 초기화 (첫 번째 전구를 눌렀으니까 1)

temp_before[0] = not temp_before[0]  # 첫 번째 전구 상태 변경
temp_before[1] = not temp_before[1]  # 두 번째 전구 상태 변경

for i in range(1, N):
    if temp_before[i - 1] != after[i - 1]:  # 이전 전구 상태가 다르면
        cnt += 1  # 스위치 조작 횟수 증가
        temp_before[i] = int(not temp_before[i])  # 현재 전구 상태 변경
        temp_before[i - 1] = int(not temp_before[i - 1])  # 이전 전구 상태 변경
        if i != N - 1:
            temp_before[i + 1] = int(not temp_before[i + 1])  # 다음 전구 상태 변경
else:
    if ''.join(map(str, temp_before)) == ''.join(map(str, after)):  # 목표 상태와 일치하면
        print(cnt)  # 조작 횟수 출력
        exit()  # 프로그램 종료

print(-1)  # 두 경우 모두 실패하면 -1