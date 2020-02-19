import sys
sys.stdin = open("input (4).txt", "r")

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(i,j):
    result_stack.append(miro[i][j])
    miro[i][j] = '-'
    for z in range(4):
        r = i + dr[z]
        c = j + dc[z]
        if miro[r][c] == 0 :
            dfs(r,c)
        elif miro[r][c] == 3:
            result_stack.append(3)

for _ in range(1,11):
    tc = int(input())
    miro = [list(map(int,input())) for _ in range(16)]

    result_stack = []
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                dfs(i,j)
                break
    print(result_stack)
    if 3 in result_stack:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))