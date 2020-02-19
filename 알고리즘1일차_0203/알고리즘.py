R,C= map(int,input().split())
result = []
for i in range(R):
    arr = list(map(int, input().split()))
    result.append(arr)

result2 = []
li2 = list(input())
for i in range(R):
    result2.append(li2[0:4])
    for j in range(4):
        li2.remove(li2[0])

for i in range(R):
    print(result[i])

for i in range(R):
    print(result2[i])
