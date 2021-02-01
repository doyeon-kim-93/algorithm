import heapq
def solution(jobs):
    jobs.sort(key=lambda x:(x[0],x[1]))
    N,answer = len(jobs),[]
    currentSec = -1
    compSec = jobs[0][0]
    visit = [0]*N
    wait = []
    while len(answer)<N:
        for i in range(N):
            if visit[i] == 0:
                if currentSec < jobs[i][0] <= compSec:
                    heapq.heappush(wait,[jobs[i][1],jobs[i][0]])
                    visit[i] = 1
        if wait:
            working,start = heapq.heappop(wait)
            answer += [compSec-start+working]
            currentSec = compSec
            compSec = compSec + working
        else:
            compSec += 1
    return sum(answer)//N

print(solution([[0, 3], [1, 9], [2, 6]]))               # 9
print()
print(solution([[0, 3], [4, 3], [10, 3]]))              # 3
print()
print(solution([[0, 10], [2, 3], [9, 3]]))              # 9
print()

print(solution([[1, 10], [3, 3], [10, 3]]))             # 9
print()

print(solution([[0, 10]]))                              # 10
print()

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))   # 15
print()

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))   # 74
print()

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74
print()
