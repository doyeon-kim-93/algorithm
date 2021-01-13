from collections import deque

def check(n,arr):
    q = deque([])
    visit = [0] * n
    q += [arr[0]]
    result = []
    while q:
        cnt = 0
        val = q.popleft()
        for i in range(n):
            if visit[i] == 0:
                if val >= arr[i]:
                    cnt += 1
                    visit[i] = 1
                else:
                    q += [arr[i]]
                    break
        result += [cnt]
    return result

def solution(progresses, speeds):
    days = []
    N = len(progresses)
    if N == 0:
        return []
    else:
        for i in range(N) :
            cnt = 0
            val = progresses[i]
            while 1:
                if val >= 100:
                    days += [cnt]
                    break
                else:
                    val += speeds[i]
                    cnt += 1
        answer = check(N,days)
    return answer

a1 = [93, 30, 55]
b1 = [1, 30, 5]

a2 = [95, 90, 99, 99, 80, 99]
b2 = [1, 1, 1, 1, 1, 1]

print(solution(a1,b1))
print(solution(a2,b2))