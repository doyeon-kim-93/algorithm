import sys
sys.stdin = open("input (9).txt", "r")

T = int(input())
N = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    con = []
    for i in range(N-1):
        for j in range(1+i,N):
            M = arr[i]*arr[j]
            con.append(M)

    con2 = list(map(str,con))
    result =[]
    flag =False
    for i in range(len(con2)):
        if con2[i] != con2[i][0]:
            for j in range(len(con2[i])-1):
                if int(con2[i][j]) <= int(con2[i][j+1]):
                    flag = True
                else:
                    flag = False
                    break

            if flag:
                result.append(int(con2[i]))

    if len(result) == 0:
        result2 = '-1'
    else:
        result2 = max(result)

    print('#{} {}'.format(tc, result2))