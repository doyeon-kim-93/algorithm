dr = [1,-1,0,0]
dc = [0,0,-1,1]

def chek():
    global result
    for _ in range(4001):
        point = {}
        for j in range(atomN):
            if atom[j][3] != 0:
                atom[j][0] += dc[atom[j][2]]
                atom[j][1] += dr[atom[j][2]]
                if abs(atom[j][0]) <= 2000 and abs(atom[j][1]) <= 2000:
                    if (atom[j][0],atom[j][1]) not in point:
                        point[(atom[j][0],atom[j][1])] = j
                    else:
                        result += (atom[j][3]+atom[point[(atom[j][0],atom[j][1])]][3])
                        atom[j][3] = 0
                        atom[point[(atom[j][0],atom[j][1])]][3]  = 0
T = int(input())
for tc in range(1,T+1):
    atomN = int(input())
    atom = []
    for i in range(atomN):
        x,y,dir,value = map(int,input().split())
        atom.append([2*x,2*y,dir,value])
    result = 0
    chek()
    print('#{} {}'.format(tc,result))