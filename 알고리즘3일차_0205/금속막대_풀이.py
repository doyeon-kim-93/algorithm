import sys
sys.stdin = open("input (9).txt", "r")

def make_bar(start):
    conn = [screw[start]]
    use = [0] * N
    use[start] = 1

    for i in range(N-1):
        isok = False
        for j in range(N):
            if use[j] == 0 and conn[i][1] == screw[j][0]:
                conn.append(screw[j])
                use[j] = 1
                isok = True
                break
        if not isok:
            break

    return  conn

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    line = list(map(int,input().split()))

    #나사를 담을 빈 리스트를 하나 만들어놓겠습니다.
    screw = [0]*N

    idx = 0
    for i in range(0,len(line),2):
        screw[idx] = [line[i],line[i+1]]
        idx += 1

    ans = []
    for i in range(N):
        tmp = make_bar(i)
        if len(ans) < len(tmp):
            ans = tmp
    print("#{}".format(tc), end=" ")
    for i in range(N):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")
    print()
