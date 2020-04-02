N = int(input())
arr = [0 for _ in range(301)]
su = [0 for _ in range(301)]
for i in range(N):
    arr[i] = int(input())
su[0] = arr[0]
su[1] = arr[0] + arr[1]
su[2] = max(arr[2]+arr[0],arr[2]+arr[1])
for i in range(3,N):
    su[i] = max(arr[i]+su[i-2],arr[i]+arr[i-1]+su[i-3])
print(su[N-1])