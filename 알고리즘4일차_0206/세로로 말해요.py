T = int(input())
for tc in range(1,T+1):
    arr = [input() for _ in range(5)]
    board = [[0]*15 for _ in range(5)]
    for i in range(5):
        for j in range(len(arr[i])):
            board[i][j] = arr[i][j]
    max_len = 0
    for i in range(len(arr)):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])

    result = []
    for i in range(max_len):
        for j in range(5):
            if board[j][i] != 0:
                result.append(arr[j][i])

    print('#{}'.format(tc),end=' ')
    for i in range(len(result)):
        print(result[i],end='')
    print()