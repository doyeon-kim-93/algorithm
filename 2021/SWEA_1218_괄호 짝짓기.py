for tc in range(1,11):
    N = int(input())
    arr = list(map(str, input()))

    result = []
    flag = 0
    for i in arr:
        if i == '(':
            result.append(1)
        elif i == '{':
            result.append(2)
        elif i == '[':
            result.append(3)
        elif i == '<':
            result.append(4)
        else:
            if result[len(result) - 1] == 1 and i == ')':
                del (result[len(result) - 1])
            elif result[len(result) - 1] == 2 and i == '}':
                del (result[len(result) - 1])
            elif result[len(result) - 1] == 3 and i == ']':
                del (result[len(result) - 1])
            elif result[len(result) - 1] == 4 and i == '>':
                del (result[len(result) - 1])
            else:
                print("#{} {}".format(tc,0))
                flag = 1
                break
    if flag == 0:
        print("#{} {}".format(tc, 1))