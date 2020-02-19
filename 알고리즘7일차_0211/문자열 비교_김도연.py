T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()
    con = 0
    for i in range(len(M)-len(N)+1):
        cnt=0
        for j in range(len(N)):
            if N[j] == M[i+j]:
                cnt += 1
            else:
                cnt = 0
        if cnt == len(N):
            con += 1
    if con >= 1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
