T = int(input())
for n in range(1,T+1):
    a =int(input())
    li=input()
    card=[]
    for i in li:
        card.append(i)     
    result={}
    for k in range(a):
        if card[k] in result:
            result[card[k]] += 1
        else:
            result[card[k]] = 1 
    val=list(result.values())
    key_=list(result.keys())
    result2=[0]
    for key, value in result.items():
        if max(val) == value:
            x = key
            y = value
            result2[-1]=int(x)
            for key2, value2 in result.items():
                if y == value2:
                    if int(key2)>int(key):
                        if result2[-1]<=int(key2):
                            result2[-1]=int(key2) 

    result_key = str(result2[0])
    print(f'#{n} {result_key} {result[result_key]} ')

          



        








  