def solution(routes):
    routes.sort()
    result = [routes[0]]

    for i in range(1,len(routes)):
        if result[-1][1] >= routes[i][0]:
            result[-1][0] = max(result[-1][0],routes[i][0])
            result[-1][1] = min(result[-1][1],routes[i][1])
        else:
            result += [routes[i]]
    return len(result)

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))