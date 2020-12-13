def up2048(arr):
    for i in range(N):
        idx = 0
        for j in range(1,N):
            if arr[j][i] != 0:
                tmp = arr[j][i]
                arr[j][i] = 0
                if arr[idx][i] == tmp:
                    arr[idx][i] = tmp * 2
                    idx += 1
                elif arr[idx][i] == 0:
                    arr[idx][i] = tmp
                else:
                    idx += 1
                    arr[idx][i] = tmp
    return arr

def down2048(arr):
    for i in range(N):
        idx = N-1
        for j in range(N-2,-1,-1):
            if arr[j][i] != 0:
                tmp = arr[j][i]
                arr[j][i] = 0
                if arr[idx][i] == tmp:
                    arr[idx][i] = tmp * 2
                    idx -= 1
                elif arr[idx][i] == 0:
                    arr[idx][i] = tmp
                else:
                    idx -= 1
                    arr[idx][i] = tmp
    return arr

def left2048(arr):
    for i in range(N):
        idx = 0
        for j in range(1,N):
            if arr[i][j] != 0:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][idx] == tmp:
                    arr[i][idx] = tmp * 2
                    idx += 1
                elif arr[i][idx] == 0:
                    arr[i][idx] = tmp
                else:
                    idx += 1
                    arr[i][idx] = tmp
    return arr


def right2048(arr):
    for i in range(N):
        idx = N-1
        for j in range(N-2,-1,-1):
            if arr[i][j] != 0:
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][idx] == tmp:
                    arr[i][idx] = tmp * 2
                    idx -= 1
                elif arr[i][idx] == 0:
                    arr[i][idx] = tmp
                else:
                    idx -= 1
                    arr[i][idx] = tmp
    return arr

def dfs(board,k):
    global result
    if k == 5:
        for i in range(N):
            result = max(result, max(board[i]))
        return
    else:
        dfs(up2048([x[:] for x in board]),k+1)
        dfs(down2048([x[:] for x in board]),k+1)
        dfs(left2048([x[:] for x in board]),k+1)
        dfs(right2048([x[:] for x in board]),k+1)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
dfs(arr,0)
print(result)

