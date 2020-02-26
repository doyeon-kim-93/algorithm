T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_line = [list(map(int,input().split())) for _ in range(N)]
    P = int(int(input()))
    bus_stop = [0] * 5001
    bus_cnt = {}
    for i in range(N):
        for j in range(bus_line[i][0],bus_line[i][1]+1):
            bus_stop[j] += 1
    print('#{}'.format(tc) , end = ' ')
    for z in range(P):
        if z == P-1:
            print(bus_stop[int(input())])
        else:
            print(bus_stop[int(input())],end = ' ')



