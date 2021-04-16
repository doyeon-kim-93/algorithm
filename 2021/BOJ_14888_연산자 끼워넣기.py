def check(idx,n):
    global num,cal,minresult,maxresult,start
    if idx >= n:
        val = start
        for i in range(len(num)):
            caln = cal[i]
            v2 = num[i]
            if caln == 0:
                val += v2
            elif caln == 1:
                val -= v2
            elif caln == 2:
                val *= v2
            elif caln == 3:
                tmp = abs(val) // v2
                if val < 0:
                    val = (-1) * tmp
                else:
                    val = tmp
        minresult = min(minresult,val)
        maxresult = max(maxresult,val)
        return
    for z in range(idx,n):
        cal[z], cal[idx] = cal[idx], cal[z]
        check(idx+1,n)
        cal[z], cal[idx] = cal[idx], cal[z]

N = int(input())
numInput = list(map(int,input().split()))
calInput = list(map(int,input().split()))
start = numInput[0]
num = numInput[1:]
cal = []
for i,val in enumerate(calInput):
    if val:
        for z in range(val):
            cal += [i]
minresult = 1000000000
maxresult = -1000000000
check(0,N-1)
print(maxresult)
print(minresult)