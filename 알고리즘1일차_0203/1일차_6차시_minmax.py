def my_min(b):
    result=b[0]
    for i in b:
        if result>i:
            result=i
    return result

def my_max(b):
    result=b[0]
    for i in b:
        if result<i:
            result=i
    return result

t=int(input())
for tc in range(1, t + 1):
    N = int(input())
    li = list(map(int, input().split()))
    result_ = my_max(li) - my_min(li)
    print(f'#{tc} {result_}')
