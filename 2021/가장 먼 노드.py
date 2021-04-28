import heapq

def dijkstra(graph, start):
    global mygraph
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

def solution(n, edge):
    global mygraph
    mygraph = {}
    for i in range(1,n+1):
        mygraph[i] = {}
    for v1,v2 in edge:
        mygraph[v1][v2] = 1
        mygraph[v2][v1] = 1
    distance = dijkstra(mygraph, 1)
    resultList = [0] * (n+1)
    for key, val in distance.items():
        resultList[key] = val
        if val == float('inf'):
            resultList[key] = -1
    maxval = max(resultList)
    return resultList.count(maxval)
mygraph = {}

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))