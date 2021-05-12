T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    left,right = 1, max(arr)
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in arr:
            total += i // mid
        if total < m:
            right = mid - 1
        else:
            left = mid + 1
    print('#{} {}'.format(tc,right))