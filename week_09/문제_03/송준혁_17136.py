# https://www.acmicpc.net/problem/17136

## Referenced
# https://chldkato.tistory.com/167

import sys

input = sys.stdin.readline
grid = [list(map(int, input().split())) for _ in range(10)]
result = 10**3

# 5개 크기 색종이의 사용 개수 추척 리스트
papers = [0] * 5


def cover(r, c, count):
    global result

    # 열 좌표 검사 완료: 탐색 종료 -> 최소값 갱신
    if c >= 10:
        result = min(result, count)
        return

    # 행 좌표 검사 완료: 다음 열 검사
    if r >= 10:
        cover(0, c + 1, count)
        return

    # 색종이를 붙여야 할 경우
    if grid[r][c] == 1:
        # 5가지의 색종이를 붙일 경우를 탐색
        for p in range(5):
            # 이미 특정 크기를 모두 사용했을 경우
            if papers[p] == 5:
                continue

            # 붙인 뒤에 칸의 경계를 넘어갔을 경우
            if r + p >= 10 or c + p >= 10:
                continue

            # 색종이를 붙인 뒤에 붙이면 안되는 곳인지 확인
            not_placable = False
            for i in range(r, r + p + 1):
                if not_placable:
                    break
                for j in range(c, c + p + 1):
                    if grid[i][j] == 0:
                        not_placable = True
                        break

            # 색종이를 붙였을 경우 붙인 부위는 다시 못붙이게함
            if not not_placable:
                for i in range(r, r + p + 1):
                    for j in range(c, c + p + 1):
                        grid[i][j] = 0

                # 사용한 크기의 색종이 개수를 증가시킨 후 재귀 진입
                papers[p] += 1
                cover(r + p + 1, c, count + 1)

                # 재귀 종료 후 사용한 색종이 개수와 못붙이게 한 범위를 복원
                papers[p] -= 1
                for i in range(r, r + p + 1):
                    for j in range(c, c + p + 1):
                        grid[i][j] = 1
    # 못붙일 경우 다음 행 검사
    else:
        cover(r + 1, c, count)


cover(0, 0, 0)
print(result if result != 10**3 else -1)
