def solution(operations):
    answer = []
    q = []
    for operation in operations:
        if operation[0] == 'I':
            q += [int(operation[2:])]
        elif q and operation[0] == 'D':
            if int(operation[2:]) == 1:
                idx = q.index(max(q))
                q.pop(idx)
            else:
                idx = q.index(min(q))
                q.pop(idx)
    if not q :
        return [0,0]
    else:
        answer += [max(q)]
        answer += [min(q)]
        return answer