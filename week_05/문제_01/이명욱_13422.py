# 투 포인터
# 리스트에 순차적으로 접근해야 할 때 두 개의 점 위치를 기록하면서 처리하는 알고리즘
# 이중 for문의 경우 시간 초과

T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    # 0 ~ M-1 까지의 합(초기)
    sm = sum(lst[0:M])
    # 시작 인덱스
    start = 0
    # 끝 인덱스
    end = M

    # cnt = 돈을 훔치는 경우의 수
    # 예외 처리 : N과 M이 같을 경우 한번만 확인
    if N == M:
        # 최소양의 돈보다 작을 때
        if sm < K:
            cnt = 1
        # 최소양의 돈보다 클 때
        else:
            cnt = 0
    else:
        cnt = 0
        while start < N:
            # 시작, 끝 한칸씩 이동하여 합 구하기
            sm -= lst[start]
                # 리스트 마지막 부분에서 인덱스가 N보다 커질 경우 나머지로
            sm += lst[end % N]
            # 최소양의 돈 보다 작을 때 경우의 수 1 증가
            if sm < K:
                cnt += 1
            # 다음 확인을 위해 인덱스 1 증가
            start += 1
            end += 1
    print(cnt)


