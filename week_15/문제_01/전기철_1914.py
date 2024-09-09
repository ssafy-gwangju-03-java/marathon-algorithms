# 1914 하노이탑
n = int(input())
def hanoi(a, b, c, d):  # b 위치에 있는 a층 높이 탑을 d층으로 이동시키는 함수
    if a == 1:
        print(b, d)
    else:
        hanoi(a - 1, b, d, c)  # a-1층을 2번으로 보내기 -> 1 a-1 0
        print(b, d)  # a를 3번으로 보내기 - 출력 -> 0 a-1 1
        hanoi(a - 1, c, b, d)  # 2번에 있던 a-1층을 3번으로 보내기 -> 0 0 a
if n > 20:
    print(2**n - 1)  # 총 횟수는 2**n -1 고정
else:
    print(2**n - 1)
    hanoi(n, 1, 2, 3)
