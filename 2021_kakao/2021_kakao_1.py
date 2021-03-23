def solution(new_id):
    step1 = new_id.lower()
    # print('step1 = ',step1)
    step2 = ''
    isok = ["-","_","."]
    for i in step1:
        if i in isok:
            step2 += i
        elif i.isalpha():
            step2 += i
        elif i.isdigit():
            step2 += i
    # print('step2 = ', step2)
    step3 = ''
    cnt = 0
    for i in step2:
        if i == '.':
            if cnt == 0:
                step3 += i
                cnt +=1
        else:
            cnt = 0
            step3 += i
    # print('step3 = ', step3)
    step4 = ''
    for i,val in enumerate(step3):
        if i == 0 or i == (len(step3)-1):
            if val != ".":
                step4 += val
        else:
            step4 += val
    # print('step4 = ', step4)
    step5 = step4
    if step5 == '':
        step5 = 'a'
    # print('step5 = ', step5)
    step6 = step5
    if len(step6) >= 16:
        step6 = step6[:15]
    if step6[-1] == '.':
        step6 = step6[:len(step6)-1]
    # print('step6 = ', step6)
    step7 = step6
    if len(step7) <= 2:
        while len(step7) < 3:
            step7 += step7[-1]

    answer = step7
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
