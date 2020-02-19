li = ['단무지','햄','참치','돈까스']
N = len(li)
for i in range(1<<N):
    for j in range(N):
        if i & (1<<j) :
            print(li[j], end=" ")
    print('김밥')
