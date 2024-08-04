# 색종이 붙이기

paper = [list(map(int, input().split())) for _ in range(10)]
use_paper = [0] * 5
min_paper = 1e9


# 색종이를 붙일 수 있는지 확인하는 함수
def check_paper_size(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if i >= 10 or j >= 10 or paper[i][j] == 0:
                return False

    return True


# 색종이를 붙이거나 떼는 함수
def attach_paper(x, y, size, num):
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = num


def check(i, j, count):
    global min_paper

    # count가 최솟값이 아니면 return
    if count >= min_paper:
        return

    # 전부 다 봤을 때
    if i >= 10:
        min_paper = min(min_paper, count)
        return

    # 그 줄이 끝나면 다음 줄로 넘어가기
    if j >= 10:
        check(i + 1, 0, count)
        return

    # 색종이 붙이기
    if paper[i][j] == 1:
        for size in range(5, 0, -1):
            # 각 색종이는 5개씩 사용 가능 && 색종이를 붙일 수 있으면
            if use_paper[size - 1] < 5 and check_paper_size(i, j, size):
                attach_paper(i, j, size, 0)
                use_paper[size - 1] += 1
                check(i, j + size, count + 1)
                # 원상태로 돌려주기
                attach_paper(i, j, size, 1)
                use_paper[size - 1] -= 1

    # 1이 아니면 다음 칸으로 이동
    else:
        check(i, j + 1, count)


check(0, 0, 0)

if min_paper == 1e9:
    print(-1)
else:
    print(min_paper)
