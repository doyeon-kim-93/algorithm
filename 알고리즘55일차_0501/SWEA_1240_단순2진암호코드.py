def scan():
    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == '1':
                code = []
                for z in range(j-56+1,j,7):
                    code.append(pre_code[arr[i][z:z+7]])
                a = code[0]+code[2]+code[4]+code[6]
                b = code[1]+code[3]+code[5]+code[7]
                if (a*3+b)%10 == 0:
                    return a+b
                else:
                    return 0
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    pre_code = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,
            '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    result = scan()
    print('#{} {}'.format(tc,result))