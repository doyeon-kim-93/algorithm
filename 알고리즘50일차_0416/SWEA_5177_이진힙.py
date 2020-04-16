T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0] + list(map(int,input().split()))
    for i in range(1,N+1):
        root = i//2
        while root >= 1:
            if arr[root]>arr[i]:
                arr[root],arr[i] = arr[i],arr[root]
            root = root //2
            i = i//2
    result = 0
    upnode = N//2
    while upnode >= 1:
        result += arr[upnode]
        upnode = upnode//2
    print('#{} {}'.format(tc,result))