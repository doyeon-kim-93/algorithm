def solution(n, computers):
    anser = 1
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            q = [i]
            visit[i] = anser
            while q:
                idx = q.pop(0)
                for j in range(n):
                    if computers[idx][j] == 1 and visit[j] == 0:
                        q += [j]
                        visit[j] = anser
            anser += 1
    return anser-1