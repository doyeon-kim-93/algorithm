def plus(k):
    global result
    if k == N :
        result += 1
        return
    else:
        if k+li[0] > N:
            return
        else:
            plus(k+li[0])
        if k+li[1] > N:
            return
        else:
            plus(k+li[1])
        if k+li[2] > N:
            return
        else:
            plus(k+li[2])

T = int(input())
for tc in range(1,T+1):
    li = [10,20,20]
    N = int(input())
    result = 0
    plus(0)
    print('#{} {}'.format(tc,result))