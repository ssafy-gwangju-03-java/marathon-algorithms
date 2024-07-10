# 월드컵

'''
input
5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4

output
1 1 0 0
'''

combination = []
for i in range(6):
    for j in range(i + 1, 6):
        combination.append([i, j])

def match(count, win, draw, lose):
    global result
    if count == 15:
        if win.count(0) == 6 and draw.count(0) == 6 and lose.count(0) == 6:
            result = 1
            return

    home, away = combination[count]

    if win[home] > 0 and lose[away] > 0:
        win[home] -= 1
        lose[away] -= 1
        match(count + 1, win, draw, lose)
        win[home] += 1
        lose[away] += 1
    
    if draw[home] > 0 and draw[away] > 0:
        draw[home] -= 1
        draw[away] -= 1
        match(count + 1, win, draw, lose)
        draw[home] += 1
        draw[away] += 1

    if lose[home] > 0 and win[away] > 0 :
        lose[home] -= 1
        win[away] -= 1
        match(count + 1, win, draw, lose)
        lose[home] += 1
        win[away] += 1

for _ in range(4):
    input_lst = list(map(int, input().split()))

    win = []
    draw = []
    lose = []

    if len(input_lst) != 18:
        print(0, end=' ')
        continue

    for idx in range(0, 18, 3):
        win.append(input_lst[idx])
        draw.append(input_lst[idx + 1])
        lose.append(input_lst[idx + 2])
    
        if input_lst[idx] + input_lst[idx + 1] + input_lst[idx + 2] != 5:
            print(0, end=' ')
            break
    
    else:
        result = 0
        match(0, win, draw, lose)
        print(result, end=' ')