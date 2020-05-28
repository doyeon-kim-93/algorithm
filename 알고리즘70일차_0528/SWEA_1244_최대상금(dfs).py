def dfs(k):
    global result
    if k == change:
        result = max(result,int(''.join(num)))
        return
    else:
        for i in range(n-1):
            for j in range(i+1,n):
                num[i],num[j] = num[j],num[i]
                if int(''.join(num)) not in  visit[k]:
                    visit[k].add(int(''.join(num)))
                    dfs(k + 1)
                num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1,T+1):
    number,change = input().split()
    num = list(number)
    n = len(num)
    change = int(change)
    visit = [set() for _ in range(change)]
    result = 0
    dfs(0)
    print('#{} {}'.format(tc,result))