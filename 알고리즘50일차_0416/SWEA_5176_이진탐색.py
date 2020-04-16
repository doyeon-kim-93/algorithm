def binary(n, last):
    global cnt
    if n <= last:
        binary(n * 2, last)
        tree[n] = cnt
        cnt += 1
        binary(n * 2 + 1, last)

for tc in range(int(input())):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    binary(1, N)
    print('#{} {} {}'.format(tc+1, tree[1], tree[N // 2]))
