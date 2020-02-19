import sys
sys.stdin = open("GNS_test_input.txt", "r")

def int_cha(n):
    dic_A = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    for key, value in dic_A.items():
        if n == key :
            n = value
    return n

def str_cha(n):
    dic_A = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    for key, value in dic_A.items():
        if n == value :
            n = key
    return n

T = int(input())
for tc in range(1,T+1):
    a,b = map(str,input().split())
    N = int(b)
    arr = list(map(str,input().split()))
    for i in range(N):
        arr[i] = int_cha(arr[i])
    arr2 = sorted(arr)

    for i in range(N):
        arr2[i] = str_cha(arr2[i])
    print('#{}'.format(tc))
    print(' '.join(arr2))
    print()