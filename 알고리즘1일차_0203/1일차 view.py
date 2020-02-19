for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    result = 0
    for i in range(2, N - 2):
        if li[i] > li[i - 1] and li[i] > li[i - 2] and li[i] > li[i + 1] and li[i] > li[i + 2]:
            a = []
            a.append(li[i] - li[i - 1])
            a.append(li[i] - li[i - 2])
            a.append(li[i] - li[i + 1])
            a.append(li[i] - li[i + 2])
            t =min(a)
            result += t
    print(f'#{tc} {result}')