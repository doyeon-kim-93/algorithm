def chek(k):
    global result,con
    if k == 12:
        result = max(result,con)
        return
    else:
        for i in range(11):
            for z in range(k):
                if visit[i][z] == 0 and player[i] == 0 and position[z] == 0 and arr[i][z] != 0:
                    visit[i][z] = 1
                    player[i] = 1
                    position[z] = 1
                    con += arr[i][z]
                    chek(k+1)
                    visit[i][z] = 0
                    player[i] = 0
                    position[z] = 0
                    con -= arr[i][z]

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(11)]
    visit = [[0]*11 for _ in range(11)]
    con = 0
    result = 0
    player = [0] * 11
    position = [0] * 11
    chek(1)
    print(result)