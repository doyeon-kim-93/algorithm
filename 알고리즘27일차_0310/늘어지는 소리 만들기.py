T = int(input())
for tc in range(1,T+1):
    word = list(input())
    N = int(input())
    index = list(map(int,input().split()))
    check = [0] * (len(word)+1)
    for i in range(N):
        check[index[i]] += 1
    print("#{} ".format(tc),end = "")
    for i in range(len(word)+1):
        if i < len(word):
            print("{}{}".format('-'*check[i],word[i]),end= "")
        else:
            print("{}".format('-' * check[i]), end="")
    print()


