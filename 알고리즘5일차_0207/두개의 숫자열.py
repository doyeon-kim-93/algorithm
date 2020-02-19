import sys
sys.stdin = open("input (12).txt", "r")

T = int(input())
for tc in range(1,T+1):
    M,N = map(int,input().split())
    Mli = list(map(int,input().split()))
    Nli = list(map(int,input().split()))
    ran = abs(M-N)
    max_re = 0
    if M > N:
        for i in range(ran+1):
            sum2 = 0
            for k in range(N):
                sum2 += Nli[k] * Mli[i+k]
            if max_re < sum2 :
                max_re = sum2
    elif M < N:
        for i in range(ran+1):
            sum2 = 0
            for k in range(M):
                sum2 += Mli[k] * Nli[i + k]
            if max_re < sum2 :
                max_re = sum2
    else:
        sum2 = 0
        for k in range(N):
            sum2 += Mli[k] * Nli[k]
        if max_re < sum2:
            max_re = sum2

    print('#{} {}'.format(tc,max_re))