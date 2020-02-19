T = int(input())
for tc in range(1,T+1):
    arr = input()
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
        elif arr[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(arr[i])
    print('#{} {}'.format(tc, len(stack)))

