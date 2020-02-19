T = int(input())
for tc in range(1,T+1):
    word = input()
    N = len(word)
    arr = [['.']*((4*N)+1) for _ in range(5)]

    for i in range(N):
        arr[2][(4*i)+2] = word[i]

    dc = [0,-1,1,-2,2,-1,1,0]
    dr = [-2,-1,-1,0,0,1,1,2]

    for j in range(N):
        for i in range(len(dr)):
            arr[2+dr[i]][((4*j)+2)+dc[i]] = '#'

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print("{}".format(arr[i][j]), end="")
        print()

