T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M-1):
        numbers = list(map(int, input().split()))
        for i in range(len(arr)):
            if numbers[0] < arr[i]:
                arr[i:i] = numbers
                break
        else:
            arr += numbers
    print('#{}'.format(tc), end=' ')
    for i in range(1,11):
        if i == 10:
            print(arr[-i])
        else:
            print(arr[-i],end = ' ')
