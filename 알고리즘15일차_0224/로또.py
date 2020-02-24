def lotto(t,T):
    if t == 6 :
        cnt = 0
        for i in range(6):
            if 0<= i+1 < 6:
                if result[i] >= result[i+1]:
                    break
                else:
                    cnt += 1
        if cnt == 5:
            print(' '.join(map(str,result)))
            return
    else:
        for i in range(k):
            if visit[i] == 0 and S[i] not in result:
                visit[i] = 1
                result.append(S[i])
                lotto(t+1,T)
                visit[i] = 0
                result.pop()

while 1:
    S = list(map(int,input().split()))
    k = S.pop(0)
    if len(S) == 0:
        break
    visit = [0] * k
    con = len(S) - 6
    for i in range(con+1):
        result = [S[i]]
        lotto(1,S[i])
    print()