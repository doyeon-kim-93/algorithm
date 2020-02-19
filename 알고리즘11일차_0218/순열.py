# #중복순열
# arr = 'ABC'
# N = len(arr)
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             print(arr[i],arr[j],arr[k])
# print()
#
# #순열
# arr = 'ABC'
# N = len(arr)
# for i in range(N):
#     for j in range(N):
#         if i == j: continue
#         for k in range(N):
#             if k == i or k == j: continue
#             print(arr[i],arr[j],arr[k])
# print()

# arr = 'ABC'
# N = len(arr)
# visit = [0] * N  #이전에 선택한 요소들에 대한 정보
# order = []
# def backtrack(k):   #k : 함수 호출트리에서 높이, 선택한 요소의 수
#     if k == N :     #단말노드의 도착, 모든 선택이 끝났다.
#         print(order)        #order에 하나의 순열이 저장된 상태
#     else:           #아직 해야할 선택이 남은 상태
#         for i in range(N):
#             if visit[i]: continue
#             visit[i] = 1
#             order.append(arr[i])        #i번 요소를 선택
#             backtrack(k+1)
#             order.pop()
#             visit[i] = 0
# backtrack(0)
# print()

#***백트래킹 순열1***
# arr = 'ABC'
# N = len(arr)
# visit = [0] * N  #이전에 선택한 요소들에 대한 정보
# order = []
# def backtrack(k):   #k : 함수 호출트리에서 높이, 선택한 요소의 수
#     if k == N :     #단말노드의 도착, 모든 선택이 끝났다.
#         print(order)        #order에 하나의 순열이 저장된 상태
#     else:           #아직 해야할 선택이 남은 상태
#         for i in range(N):
#             if visit[i]: continue
#             visit[i] = 1
#             order.append(arr[i])        #i번 요소를 선택
#             backtrack(k+1)
#             order.pop()
#             visit[i] = 0
# backtrack(0)

#백트래킹 순열2 - 비트표현
arr = 'ABC'
N = len(arr)
# visit = [0] * N  #이전에 선택한 요소들에 대한 정보
order = []
def backtrack(k, visit):   #k : 함수 호출트리에서 높이, 선택한 요소의 수
    if k == N :     #단말노드의 도착, 모든 선택이 끝났다.
        print(order)        #order에 하나의 순열이 저장된 상태
    else:           #아직 해야할 선택이 남은 상태
        for i in range(N):
            if visit & (1<<i): continue
            order.append(arr[i])        #i번 요소를 선택
            backtrack(k+1,visit | (1<<i))
            order.pop()
backtrack(0,0)