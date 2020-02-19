# ver1
arr = [i for i in range(1,11)]
N = len(arr)
bit = [0]*N
def backtrack(k):
    if k == N:
        S = 0
        for i in range(N):
            if bit[i]: S += arr[i]
    else:
        bit[k] = 1 ; backtrack(k+1) #k번 요소를 포함
        bit[k] = 1 ; backtrack(k + 1)  # k번 요소를 포함 하지 않음
backtrack(0)

#ver2
arr = [i for i in range(1,11)]
N = len(arr)

A = []
def backtrack(k):
    if k == N:
        if sum(A) == 10:
            print(A)
    else:
        A.append(arr[k]);
        backtrack(k+1) #k번 요소를 포함
        A.pop()
        backtrack(k + 1)  # k번 요소를 포함 하지 않음
backtrack(0)

#ver3
arr = [i for i in range(1,11)]
N = len(arr)

A = []
def backtrack(k,cur):
    if k == N:
        if sum(A) == 10:
            print(A)
    else:
        A.append(arr[k]);
        backtrack(k+1, cur + arr[k]) #k번 요소를 포함
        A.pop()
        backtrack(k + 1, cur)  # k번 요소를 포함 하지 않음
backtrack(0,0)