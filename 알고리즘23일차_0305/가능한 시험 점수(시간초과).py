def check(k,sum_,n):
    if k == n:
        result.add(sum_)
    else:
        check(k+1,sum_+arr[k],n)
        check(k+1,sum_,n)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = set()
    check(0,0,N)
    print('#{} {}'.format(tc,len(result)))