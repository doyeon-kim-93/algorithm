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
    left = 0
    right = 0
    for i in range(len(name)):
        nameList += [name[i:i+1]]
        if name[i:i+1] != 'A':
            right += i
            if i != 0:
                left += (len(name) - i)
    if right < left:
        cnt = 0
        for i in range(len(nameList)):
            if i != 0 and nameList[i] != 'A':
               cnt = max(cnt,i)
        answer += cnt
    else:
        cnt = 0
        for i in range(len(nameList)-1,-1,-1):
            if i != 0 and nameList[i] != 'A':
               cnt = max(cnt,((len(name) - i)))
        answer += cnt

    for name in nameList:
        if name != 'A':
            answer += alpha_set[name]
    return answer

print(solution('JEROEN'))
print(solution('JAN'))