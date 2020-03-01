def check(k,N):
    global result
    if k == 12 or 12<k<15 :
        if result > N:
            result = N
            return
    else:
        check(k+1, N+(price[0]*plan[k]))
        check(k+1, N+price[1])
        check(k+3, N+price[2])

T= int(input())
for tc in range(1,T+1):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    result = price[3]
    check(1,0)
    print('#{} {}'.format(tc,result))