def solution(priorities, location):
    M = location
    N = len(priorities)
    result = [-1] * N
    process = []
    for i in range(len(priorities)):
        process += [(i,priorities[i])]
    idx = 0
    while process:
        j,val = process.pop(0)
        cnt = 0
        for i,prior in process:
            if val < prior :
                process += [[j,val]]
                break
            else:
                cnt += 1
        if cnt == len(process):
            if j == M:
                return idx+1
            else:
                result[idx] = val
                idx += 1

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))