for _ in range(0,10):
    tc = int(input())
    num = list(map(int,input().split()))
    while 1:
        flag = False
        for i in range(1,6):
            A = num.pop(0)
            B = A-i
            if B <= 0:
                B = 0
                flag = True
                num.append(B)
                break
            else:
                num.append(B)
        if flag:
            break
    print('#{}'.format(tc),end = ' ')
    print(' '.join(map(str,num)))