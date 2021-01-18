def solution(citations):
    citations.sort()
    answer = 0
    for i in range(0,max(citations)):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt >= i:
            answer = max(answer,i)
    return answer