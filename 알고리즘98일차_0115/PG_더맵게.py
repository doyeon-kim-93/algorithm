import heapq
def solution(scoville, K):
    answer = 0
    N = len(scoville)
    q = []
    for i in range(N):
        heapq.heappush(q,scoville[i])
    if q[0] >= K :
        return 0
    while 1:
        if len(q) == 1:
            if q[0] < K:
                return -1
        else:
            answer += 1
            val1 = heapq.heappop(q)
            val2 = heapq.heappop(q)
            newVal = val1 + (2*val2)
            heapq.heappush(q,newVal)
            if q[0] >= K:
                return answer

print(solution([1, 2, 3, 9, 10, 12],7))