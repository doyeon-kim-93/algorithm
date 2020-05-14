def chek(k,li):
    global turn,result
    mid = (len(li)-1)//2
    if li[mid] == k:
        result += 1
        return
    else:
        left = li[:mid]
        right = li[mid+1:]
        if k < li[mid]:
            turn += 1
            chek(k,left)
        elif k > li[mid]:
            turn -= 1
            chek(k,right)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    result = 0
    num = []
    flag = True
    for i in A:
        if i in B:
            num += [i]
    if len(num) == 0:
        flag = False
    if flag:
        for z in num:
            turn = 0
            chek(z,A)
            if turn > 1 or turn < -1:
                result -= 1
    print('#{} {}'.format(tc,result))