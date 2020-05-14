def MergeSort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    if left[-1] > right[-1]:
        cnt +=1
    return Merge(left, right)

def Merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        elif j < len(arr2):
            result.append(arr2[j])
            j += 1
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    re_arr = sorted(arr)
    cnt = 0
    MergeSort(arr)
    print('#{} {} {}'.format(tc,re_arr[N//2],cnt))