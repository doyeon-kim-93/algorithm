def solution(answers):
    answer = [0] * 4
    answerLen = [5,8,10]
    answerResult = []
    for i in range(3):
        r = len(answers)//answerLen[i]
        c = len(answers)%answerLen[i]
        answerResult += [[r,c]]
    p1 = [1,2,3,4,5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answerResult)):
        if i == 0:
            p1 = p1*answerResult[i][0] +p1[:answerResult[i][1]]
        elif i == 1:
            p2 = p2 * answerResult[i][0] + p2[:answerResult[i][1]]
        else:
            p3 = p3 * answerResult[i][0] + p3[:answerResult[i][1]]
    for i in range(3):
        if i == 0:
            for j in range(len(answers)):
                if p1[j] == answers[j]:
                    answer[i+1] += 1
        elif i == 1:
            for j in range(len(answers)):
                if p2[j] == answers[j]:
                    answer[i+1] += 1
        else:
            for j in range(len(answers)):
                if p3[j] == answers[j]:
                    answer[i+1] += 1
    result = []
    maxVal = max(answer)
    for i in range(len(answer)):
        if answer[i] == maxVal:
            result += [i]
    return result

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

