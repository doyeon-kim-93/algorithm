import sys
sys.stdin = open("input (9).txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base = list(map(int,input().split()))
    even_num = []
    odd_num = []
    for i in range(2*N):
        if i%2 ==0:
            even_num.append(base[i])
        else:
            odd_num.append(base[i])

    first_num = []
    last_num = []
    for j in range(N):
        if even_num[j] not in odd_num :
            first_num.append(even_num[j])
        if odd_num[j] not in even_num :
            last_num.append(odd_num[j])

    first_num_index = base.index(first_num[0])
    last_num_index = base.index(last_num[0])

    result = [first_num[0],base[first_num_index + 1]]
    start = base[first_num_index + 1]

    li = [start]
    for i in range(N):
        T = even_num.index(li[-1])
        li.append(base[(2 * T)-1])

    for i in range(N):
        if li[i] in even_num:
            result.append(start)
        else:
            result.append(start)



