def buble(arr):
    for i in range(len(arr)-1,0,-1):
        for k in range(i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr2=list(map(int, input().split()))
    mysort = buble(arr2)
    result = []
    for i in range(0,N//2):
        result.append(mysort[-i-1])
        result.append(mysort[i])
    result2 =[]
    for j in range(10):
        result2.append(result[j])
    result3 = " ".join(map(str, result2))
    print('#{} {}'.format(tc,result3))