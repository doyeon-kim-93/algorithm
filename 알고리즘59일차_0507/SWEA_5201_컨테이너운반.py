T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    con = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    visited = [0] * M

    result = 0
    for i in range(M):
        cnt = 0
        for z in con:
            if truck[i] >= z and z >= cnt:
                cnt = z
        if cnt != 0:
            con.remove(cnt)
        result += cnt
    print('#{} {}'.format(tc,result))

