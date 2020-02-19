def game(k):
    if len(k) == 2:
        if k[0] == 1 and k[1] == 2:
            k.pop(0)
        elif k[0] == 2 and k[1] == 1:
            k.pop(1)
        elif k[0] == 1 and k[1] == 1:
            k.pop(1)
        elif k[0] == 2 and k[1] == 3:
            k.pop(0)
        elif k[0] == 3 and k[1] == 2:
            k.pop(1)
        elif k[0] == 2 and k[1] == 2:
            k.pop(1)
        elif k[0] == 3 and k[1] == 1:
            k.pop(0)
        elif k[0] == 1 and k[1] == 3:
            k.pop(1)
        elif k[0] == 3 and k[1] == 3:
            k.pop(1)
    else:
        return


def divid(k):
    if len(k) <= 2:
        li.append(k)
    else:
        r = len(k) // 2
        divid(k[0:r])
        divid(k[r:len(k) + 1])

def calc(k):
    divid(k)
    for i in range(len(li)):
        game(li[i])
    for j in range(len(li)):
        re.append(li[j][0])
    divid(re)

    if len(re) == 1:
        print(re[0])
    else:
        calc(re)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    player = list(map(int, input().split()))
    li = []
    re = []
    calc(player)
    print(li)
    print(re)