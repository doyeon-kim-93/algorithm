def chek(k,t,li):
    global result
    if k == N-1:
        con = sum(li) + arr[t][0]
        result = min(result,con)
        return
    elif sum(li) >= result:
        return
    else:
        for z in range(1,N):
            if arr[t][z] > 0 and visit[z] == 0:
                visit[z] = 1
                li += [arr[t][z]]
                chek(k+1,z,li)
                li.pop()
                visit[z] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visit = [0] * N
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit[0] = 1
    result = 987654321
    chek(0,0,[])
    print('#{} {}'.format(tc,result))