T = int(input())
for tc in range(1,T+1):
    li = list(map(int, input().split()))
    A = li[1]
    B = li[2]
    book = li[0]

    A_con = 0
    A_l = 1
    A_r = book
    i = 0
    while i != A:
        A_con += 1
        i = (A_l + A_r)//2
        if i < A:
             A_l = i
        else:
            A_r = i

    B_con = 0
    B_l = 1
    B_r = book
    i = 0
    while i != B:
        B_con += 1
        i = (B_l + B_r)//2
        if i < B:
             B_l = i
        else:
            B_r = i

    if A_con > B_con:
        print('#{} B'.format(tc))
    elif A_con < B_con:
        print('#{} A'.format(tc))
    else:
        print('#{} 0'.format(tc))