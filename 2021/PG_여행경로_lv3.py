def bfs(tmp,visit,tickets,result,cnt,N):
    global answer
    if cnt == N:
        tmp = []
        for val in result:
            tmp += [val]
        answer += [tmp]
        return
    for j,val in enumerate(tickets):
        if visit[j] == 0 and val[0] == tmp:
            visit[j] = 1
            result += [val[1]]
            bfs(val[1],visit,tickets,result,cnt+1,N)
            visit[j] = 0
            result.pop()
def solution(tickets):
    global answer
    N = len(tickets)
    for i,ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            visit = [0 for _ in range(N)]
            visit[i] = 1
            bfs(ticket[1],visit,tickets,["ICN",ticket[1]],1,N)
    answer.sort()
    return answer[0]
answer = []

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))