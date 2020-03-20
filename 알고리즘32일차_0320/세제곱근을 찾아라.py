for tc in range(1,int(input())+1):
    N = int(input())
    a = int((N ** (1.0/3.0)) + 0.1)
    if a*a*a == N :
        print("#{} {}".format(tc,a))
    else:
        print('#{} -1'.format(tc))