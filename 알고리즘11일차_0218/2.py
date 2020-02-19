# A = [64,7,4,25,10,22,11,8]
# N = len(A)
#
# def getMin(A,lo,hi): #arr 에서 최소값을 반환하는 함수
#            #재귀함수로 구현
#     #기저 사례
#     if lo == hi :
#         return A[lo]
#     #일반 사례
#     ret = getMin(A,lo,hi-1)
#     return  min(ret, A[hi])
# print(getMin(A, 0, N-1))

A = [64,7,4,25,10,22,11,8]
N = len(A)
def getMin(A,lo,hi):       
    if lo == hi :
        return A[lo]
    mid = (lo + hi) >> 1
    l = getMin(A,lo,mid)
    r = getMin(A,mid+1,hi)
    return  min(l,r)
print(getMin(A, 0, N-1))