T = int(input())
for n in range(1,T+1):
    ab =list(map(int, input().split()))
    a, b = ab[0], ab[-1] 
    li=list(map(int, input().split()))
    result = []
    for i in range(0,(a-b)+1):
        k=b
        sum_= 0
        for j in range(b):
            sum_u = li[i+j]
            sum_ += sum_u    
        result.append(sum_)    
    print(result)
    print(f'#{n} {max(result)-min(result)}')
