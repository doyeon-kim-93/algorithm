T = int(input())
for tc in range(1,T+1):
    N ,M = map(int,input().split())
    pa = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            p = 0
            for k in range(M):
                for z in range(M):
                    p.append(pa[i+k][j+M ])

            if result_ < p:
                result = p
    print('#{} {}'.format(tc,p))
#
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     Pari = [list(map(int, input().split())) for _ in range(N)]
#     Max = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             p = 0
#             for k in range(M):
#                 for l in range(M):
#                     p += Pari[i+k][j+l]
#             if p > Max:
#                 Max = p
#     print('#{} {}'.format(t, Max))