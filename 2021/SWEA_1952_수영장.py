def check(cnt,val,visit):
    global result,cost
    if cnt >= 12:
        result = min(result,val)
        return
    if val >= result:
        return
    if arr[cnt] != 0 and visit[cnt] == 0:
        for i in range(3):
            if i == 0:
                val += (arr[cnt]*cost[i])
                visit[cnt] = 1
                check(cnt+1,val,visit)
                val -= (arr[cnt] * cost[i])
                visit[cnt] = 0
            elif i == 1:
                val += cost[i]
                visit[cnt] = 1
                check(cnt+1,val,visit)
                val -= cost[i]
                visit[cnt] = 0
            else:
                val += cost[i]
                for z in range(cnt,cnt+3):
                    if z < 12:
                        visit[z] = 1
                check(cnt + 1, val, visit)
                val -= cost[i]
                for z in range(cnt,cnt+3):
                    if z < 12:
                        visit[z] = 0
    else:
        check(cnt+1,val,visit)
T = int(input())
for tc in range(1,T+1):
    costInput = list(map(int, input().split()))
    arr = list(map(int,input().split()))
    visit = [0 for _ in range(12)]
    cost = costInput[:3]
    result = costInput[-1]
    check(0,0,visit)
    print('#{} {}'.format(tc,result))