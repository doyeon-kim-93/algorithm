for tc in range(1, 11):
    N = int(input())
    arr = list(map(str, input()))
    num = list(map(str, range(10)))
    after = []
    forth = []
    for i in range(N):
        if arr[i] in num:
            after.append(int(arr[i]))
        elif arr[i] == '+':
            if forth[-1] == '*' or forth[-1] == '+':
                while 1:
                    after.append(forth.pop())
                    if forth[-1] == '(' or len(forth) == 0:
                        forth.append(arr[i])
                        break
            else:
                forth.append(arr[i])
        elif arr[i] == '*':
            forth.append(arr[i])
        elif arr[i] == '(':
            forth.append((arr[i]))
        elif arr[i] == ')':
            while 1:
                after.append(forth.pop())
                if forth[-1] == '(':
                    forth.pop()
                    break
    forth2 = ['+', '*']
    stack = []
    stack2 = []
    for i in range(len(after)):
        if after[i] not in forth2 :
            stack.append(after[i])
        elif after[i] in forth2:
            stack2.append(after[i])
            if len(stack) >= 2:
                stack2.pop()
                if after[i] == '+':
                    stack.append(int(stack.pop(-2)) + int(stack.pop(-1)))
                elif after[i] == '*':
                    stack.append(int(stack.pop(-2)) * int(stack.pop(-1)))

    print('#{} {}'.format(tc, stack.pop()))