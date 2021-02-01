from string import ascii_uppercase
def solution(name):
    answer = 0
    alpha = list(ascii_uppercase)
    alpha_set = {}
    for i in range(len(alpha)):
        if i <= (26-i):
            alpha_set[alpha[i]] = i
        else:
            alpha_set[alpha[i]] = (26-i)
    nameList = []
    for i in range(len(name)):
        nameList += [name[i:i+1]]
    resultList = []
    for name in nameList:
        resultList += [alpha_set[name]]
    idx = 0
    while 1:
        answer += resultList[idx]
        resultList[idx] = 0
        if sum(resultList) == 0:
            break
        left = 1
        right = 1
        while resultList[idx+right] == 0:
            right += 1
        while resultList[idx-left] == 0:
            left += 1
        if left >= right:
            idx += right
            answer += right
        else:
            idx -= left
            answer += left
    return answer


print(solution('JEROEN'))
print(solution('JAN'))