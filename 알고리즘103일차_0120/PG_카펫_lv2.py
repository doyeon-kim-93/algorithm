def solution(brown, yellow):
    answer = []
    for i in range((brown//2)-1,-1,-1):
        r = i
        c = (brown//2)-i
        if r >= c and r >= c+2:
            if (r-2)*c == yellow:
                answer += [r,c+2]
    return answer