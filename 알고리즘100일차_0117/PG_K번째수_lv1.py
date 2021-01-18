def solution(array, commands):
    answer = []
    cnt = 0
    while cnt != len(commands):
        i,j,z = commands[cnt]
        arr = array[i-1:j]
        arr.sort()
        answer += [arr[z-1]]
        cnt += 1
    return answer