재료 = ['단무지','햄','참치','돈가스']
bit = [0,0,0,0]
for a in range(2):
    bit[0] = a
    for b in range(2):
        bit[1] = b
        for c in range(2):
            bit[2] =c
            for d in range(2):
                bit[3] = d
                print(bit)
                for i in range(len(bit)):
                    if bit[i] ==1:
                        print(재료[i],end=' ')
                print('들어간 김밥')