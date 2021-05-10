T = int(input())
for tc in range(1, T + 1):
    li = []
    D, N = map(int, input().split())
    for _ in range(N):
        k, s = map(int, input().split())
        li.append((D - k) / s)
    result = D / max(li)
    print("#{} {}".format(tc,result))