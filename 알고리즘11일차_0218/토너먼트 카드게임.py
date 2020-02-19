def game(k):
    if len(k) == 2:
        if k[0][1] == 1 and k[1][1] == 2:
            k.pop(0)
        elif k[0][1] == 2 and k[1][1] == 1:
            k.pop(1)
        elif k[0][1] == 1 and k[1][1] == 1:
            k.pop(1)
        if k[0][1] == 2 and k[1][1] == 3:
            k.pop(0)
        elif k[0][1] == 3 and k[1][1] == 2:
            k.pop(1)
        elif k[0][1] == 2 and k[1][1] == 2:
            k.pop(1)
        if k[0][1] == 3 and k[1][1] == 1:
            k.pop(0)
        elif k[0][1] == 1 and k[1][1] == 3:
            k.pop(1)
        elif k[0][1] == 3 and k[1][1] == 3:
            k.pop(1)

def divid(k):
    if len(k) <= 2 :
        li.append(k)
    else :
        r = len(k)//2
        divid(k[0:r])
        divid(k[r:len(k)+1])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    player = list(map(int,input().split()))
    with_index =[]
    for i in range(N):
        with_index.append((i,player[i]))
    li = []
    divid(with_index)
    # for i in range(len(li)):
    #     game(li[i])
    print(li)
    print(len(li))
    print()
