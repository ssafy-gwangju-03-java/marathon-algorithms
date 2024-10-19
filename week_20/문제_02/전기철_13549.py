# 13549 숨바꼭질 3
a, b = map(int, input().split())


def hide(x, y):
    if x >= y:  # 내가 앞쪽에있음
        return x - y
    if y == 1:  # y%2 == 0이라서 처리
        return 1
    if y % 2 == 0:  # 2의배수
        return min(y - x, hide(x, y // 2))  # +1씩 해서 가까워지거나 //2에서 두배
    else:  # 2의배수 +-1
        return (min(hide(x, y - 1), hide(x, y + 1)) + 1)  # 마지막이 +1 or -1이여야야하므로 양쪽 값 +1


print(hide(a, b))
