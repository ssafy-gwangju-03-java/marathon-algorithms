T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    if N == M and sum(arr) < K:
        print(1)
        continue

    s = 0
    e = M % N
    acc = sum(arr[:M])
    answer = 0

    if acc < K:
        answer += 1

    for i in range(1, N):
        acc -= arr[s]
        acc += arr[e]

        if acc < K:
            answer += 1

        s = (s + 1) % N
        e = (e + 1) % N

    print(answer)
