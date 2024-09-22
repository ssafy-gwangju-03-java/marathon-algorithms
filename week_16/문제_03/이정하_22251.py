def onoff(nX):
    global result
    ans = 0

    if nX < 1 or nX > N:
        return  # 층수가 범위 내 아니면 끝내기

    currentX = list(f'{X:0{K}d}')  # 현재 층수를 K자리 문자열로 변환해서 리스트화하기
    currentnX = list(f'{nX:0{K}d}')  # 변경 대상 층수를 K자리 문자열로 변환해서 리스트화하기

    for i in range(K):
        currentXNum = num[currentX[i]].copy()  # 현재 층수의 i번째 자리 숫자의 LED 상태 복사하기
        currentnXNum = num[currentnX[i]].copy()  # 변경 대상 층수의 i번째 자리 숫자의 LED 상태 복사하기
        common_values = [value for value in currentXNum if value in currentnXNum]  # 두 숫자의 공통 LED 찾기
        final = [x for x in currentXNum + currentnXNum if x not in common_values]  # 변경이 필요한 LED 찾기

        ans += len(final)  # 변경이 필요한 LED 개수 누적하기

    if 0 < ans <= P:
        result += 1  # 변경 가능한 경우-> 결과 증가시키기


# N: 최대 층수, K: 자리 수, P: 최대 반전 가능 수, X: 현재 층수
N, K, P, X = map(int, input().split())  # 입력값 받아 변수에 할당하기
num = {'0': [1, 2, 3, 5, 6, 7], '1': [3, 6], '2': [1, 3, 4, 5, 7], '3': [1, 3, 4, 6, 7], '4': [2, 3, 4, 6],
       '5': [1, 2, 4, 6, 7], '6': [1, 2, 4, 5, 6, 7], '7': [1, 3, 6], '8': [1, 2, 3, 4, 5, 6, 7],
       '9': [1, 2, 3, 4, 6, 7]}  # 각 숫자의 LED 상태 정의하기
result = 0  # 결과값 초기화하기

for n in range(1, N + 1):
    onoff(n)  # 1부터 N까지의 모든 층수에 대해 onoff 함수 호출

print(result)
