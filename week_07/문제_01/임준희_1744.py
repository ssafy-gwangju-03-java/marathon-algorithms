def max_sum(numbers):
    # 양수, 음수, 1, 0
    positives = []
    negatives = []
    ones = []
    zeros = 0

    for num in numbers:
        if num > 1:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        elif num == 1:
            ones.append(num)
        else: 
            zeros += 1

    # 양수와 음수를 내림차순으로 정렬
    positives.sort(reverse=True)
    negatives.sort()

    result = 0

    # 양수들을 2개씩 묶어 곱한 후 더함
    for i in range(0, len(positives) - 1, 2):
        result += positives[i] * positives[i+1]
    if len(positives) % 2 != 0:
        result += positives[-1]

    # 음수들을 2개씩 묶어 곱한 후 더함
    for i in range(0, len(negatives) - 1, 2):
        result += negatives[i] * negatives[i+1]
    if len(negatives) % 2 != 0:
        # 남은 음수가 있고 0이 없으면 그 음수를 더함
        if zeros == 0:
            result += negatives[-1]

    # 1은 그대로 더함
    result += sum(ones)

    return result

n = int(input())
numbers = [int(input()) for _ in range(n)]

print(max_sum(numbers))