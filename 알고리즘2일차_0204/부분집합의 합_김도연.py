T = int(input())
arr=[1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1,T+1):
    n, k = map(int, input().split())
    con = 0
    for i in range(1<<len(arr)):
        result = []
        for j in range(12):
            if i&(1<<j):
                result.append(arr[j])
        if sum(result) == k and len(result) == n:
            con += 1
    print('#{} {}'.format(tc, con))



#부분집합 구해보기
