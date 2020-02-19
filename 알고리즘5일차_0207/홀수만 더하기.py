T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = len(arr)
    K = N//2
    result = arr[k]
    print('#{} {}'.format(tc,result))
