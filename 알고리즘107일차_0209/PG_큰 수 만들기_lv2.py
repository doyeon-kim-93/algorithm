def solution(number, k):
    num = []
    for i in range(len(number)):
        num += [number[i:i+1]]
    result = [num[0]]
    for i in range(1,len(num)):
        while result and int(result[-1]) < int(num[i]):
            result.pop()
            k -= 1
            if not k:
                result += num[i:]
                break
        if not k:
            break
        result += [number[i]]
    if k:
        for z in range(1,k+1):
            result.pop()
    return ''.join(result)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))

# def check(arr,visit,k,n,idx):
#     global result
#     if idx >= len(arr):
#         return
#     if n == k :
#         tmp = ''
#         for i in range(len(visit)):
#             if visit[i] == 0:
#                 tmp += arr[i]
#         result += [int(tmp)]
#         return
#     visit[idx] = 1
#     check(arr,visit,k,n+1,idx+1)
#     visit[idx] = 0
#     check(arr,visit,k,n,idx+1)
# def solution(number, k):
#     global result
#     result = []
#     num = []
#     for i in range(len(number)):
#         num += [number[i:i+1]]
#     visit = [0] * len(num)
#     check(num,visit,k,0,0)
#     return str(max(result))
# result = []