def get_max_sum(arr):
    # 배열을 입력받아 최대 곱의 합을 반환하자
    res = 0  # 결과 합을 저장
    prev = 1001  # 이전 값을 저장 / 초기값은 범위를 벗어나는 값으로 설정
    for i in range(len(arr)):  # 배열의 길이만큼 반복
        if prev == 1001:  # 초기 상태 or 짝을 이루지 못한 경우
            prev = arr[i]  # 현재 값을 prev에 저장
        else:  # 짝을 이루는 경우
            res += prev * arr[i]  # 이전 값과 현재 값을 곱하여 결과에 더함
            prev = 1001  # prev 리셋
    res += (0 if prev == 1001 else prev)  # 마지막 값이 짝을 이루지 못했다면 결과에 더함
    return res  # 최종 결과 반환


# 길이 N
N = int(input())
# 양수 음수 저장
pos = []
neg = []

ans = 0

for _ in range(N):
    tmp = int(input())
    if tmp > 1:  # 1보다 크면 양수 리스트에 추가
        pos.append(tmp)
    elif tmp == 1:  # 1은 곱할 필요 없이 결과에 더함
        ans += 1
    else:  # 0 이하의 값은 음수 리스트에 추가
        neg.append(tmp)

# 양수- 내림차순으로 정렬
pos.sort(reverse=True)
# 음수 - 오름차순으로 정렬
neg.sort()

# 양수 음수 리스트에서 최대 곱을 구하고 결과에 더함
ans += (get_max_sum(pos) + get_max_sum(neg))

print(ans)
