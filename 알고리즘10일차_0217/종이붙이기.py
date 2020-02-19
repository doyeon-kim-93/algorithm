path = []
def backtrack(k,n): #k = 함수호출의 높이, 지금까지 선택의 횟수
    if n < 0 : return
    if n == 0:      # n = 문제의 크기,
        print(path)
    else: # l , = , ll
        #내가 할 수 있는 선택은 3가지 ㅣ , = , ㅣㅣ
        path.append('l') ; backtrack(k+1,n-1); path.pop()
        path.append('=') ; backtrack(k+1,n-2); path.pop()
        path.append('ll'); backtrack(k+1,n-2); path.pop()
backtrack(0,4)