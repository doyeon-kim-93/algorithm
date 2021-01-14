def solution(bridge_length, weight, truck_weights):
    answer = 1
    N, M = bridge_length, weight
    l = len(truck_weights)
    result = []
    bridge = []
    w = 0
    while 1:
        if len(result) == l:
            break
        answer += 1
        if len(bridge) > 0:
            for i in range(len(bridge)):
                bridge[i][0] += 1
        if len(truck_weights) > 0:
            if len(bridge) < N:
                if w + truck_weights[0] <= M:
                    bridge += [[1,truck_weights[0]]]
                    w += truck_weights[0]
                    truck_weights.pop(0)
        if len(bridge) > 0:
            if bridge[0][0] >= N:
                w -= bridge[0][1]
                result += [bridge[0][1]]
                bridge.pop(0)
    return answer

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))