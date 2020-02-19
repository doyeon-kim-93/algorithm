T = int(input())
for tc in range(1,T+1):
    Ar1, Ac1, Ar2, Ac2 = map(int, input().split())
    Br1, Bc1, Br2, Bc2 = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(10)]
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    for i in range(Ar1,Ar2+1):
        for j in range(Ac1,Ac2+1):
            result1 += arr[i][j]
            con = arr[i][j] * 2
            if con >= 255 :
                con = 255
            arr[i][j] = con
            result2 += con
    for i in range(Br1,Br2+1):
        for j in range(Bc1,Bc2+1):
            result3 += arr[i][j]
            con = arr[i][j] //2
            con2 = round(con)
            if con2 <= 0  :
                con2 = 0
            arr[i][j] = con2
            result4 += con2
    result5 = abs(result1-result2)
    result6 = abs(result3-result4)
    result7 = result5 + result6
    print('#{} {}'.format(tc,result7))
