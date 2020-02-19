mark1 = ['.', '*', '#', '-']
mark2 = ['^', 'v', '<', '>']
def motion(li,i,r,c):
    if li[i] == 'U':
        arr[r][c] = mark2[0]
        if 0 <= r-1 < H:
            if arr[r-1][c] == mark1[0]:
                arr[r][c] = mark1[0]
                arr[r-1][c] = mark2[0]
    elif li[i] == 'D':
        arr[r][c] = mark2[1]
        if 0 <= r+1 < H:
            if arr[r + 1][c] == mark1[0]:
                arr[r][c] = mark1[0]
                arr[r + 1][c] = mark2[1]
    elif li[i] == 'L':
        arr[r][c] = mark2[2]
        if 0 <= c - 1 < W:
            if arr[r][c-1] == mark1[0]:
                arr[r][c] = mark1[0]
                arr[r][c-1] =mark2[2]
    elif li[i] == 'R':
        arr[r][c] = mark2[3]
        if 0 <= c + 1 < W:
            if arr[r][c+1] == mark1[0]:
                arr[r][c] = mark1[0]
                arr[r][c+1] = mark2[3]
    elif li[i] == 'S':
        if arr[r][c] == '^':
            while r > 0:
                r -= 1
                if arr[r][c] == '*':
                    arr[r][c] = '.'
                    break
                elif arr[r][c] == '#':
                    break
        elif arr[r][c] == 'v':
            while r < H-1:
                r += 1
                if arr[r][c] == '*':
                    arr[r][c] = '.'
                    break
                elif arr[r][c] == '#':
                    break
        elif arr[r][c] == '<':
            while c > 0:
                c -= 1
                if arr[r][c] == '*':
                    arr[r][c] = '.'
                    break
                elif arr[r][c] == '#':
                    break
        elif arr[r][c] == '>':
            while c < W-1:
                c += 1
                if arr[r][c] == '*':
                    arr[r][c] = '.'
                    break
                elif arr[r][c] == '#':
                    break

T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(H)]
    N = int(input())
    moti = list(input())
    for z in range(N):
        flag = False
        for i in range(H):
            for j in range(W):
                if arr[i][j] in mark2:
                    motion(moti,z,i,j)
                    flag =True
                    break
            if flag:
                break
    print('#{}'.format(tc),end = ' ')
    for i in range(H):
        for j in range(W):
            print(arr[i][j] ,end = '')
        print()