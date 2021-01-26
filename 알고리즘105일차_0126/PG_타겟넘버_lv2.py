def bfs(arr,visit,target,cnt,n,idx):
    global result
    if idx == n:
        if cnt == target:
            result += 1
        return
    if visit[idx] == 0:
        visit[idx] = 1
        bfs(arr, visit, target, cnt + arr[idx], n, idx+1)
        visit[idx] = 0
        bfs(arr, visit, target, cnt - arr[idx], n, idx + 1)
def solution(numbers, target):
    global result
    visit = [0] * len(numbers)
    bfs(numbers,visit,target,0,len(numbers),0)
    return result

result = 0
print(solution([1, 1, 1, 1, 1], 3))
