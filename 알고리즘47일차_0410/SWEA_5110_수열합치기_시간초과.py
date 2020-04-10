class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

 # <---------------------------insert---------------------------->
    def insertfirst(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            self.cnt += 1
        else:
            temp = self.head
            newnode.next = temp
            self.head = newnode
            self.cnt += 1

    def insertLast(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            self.cnt += 1
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            self.tail = newnode
            self.cnt += 1

    def insertAt(self,idx,data):
        newnode = Node(data)
        if idx >= self.cnt:
            self.insertLast(data)
        else:
            pre = None
            temp = self.head
            for _ in range(idx):
                pre = temp
                temp = temp.next
            pre.next = newnode
            newnode.next = temp
            self.cnt +=1

    def print_List(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next
    def print_lenth(self):
        if self.cnt == 0:
            print(0)
        else:
            print(self.cnt)

    def Serch(self,data):
        newnode = Node(data)
        temp = self.head
        idx = 0
        while newnode.data >= temp.data:
            idx += 1
            temp = temp.next
            if idx == self.cnt:
                break
        return idx

    def listinput(self):
        global result
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while temp != None:
                result.append(temp.data)
                temp = temp.next


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]
    link_li = Linkedlist()
    for i in range(M):
        if i == 0:
            for z in range(N):
                link_li.insertLast(arr[i][z])
        else:
            idx_ = link_li.Serch(arr[i][0])
            for z in range(N):
                if z == 0:
                    if idx_ == 0:
                        link_li.insertfirst(arr[i][z])
                    else:
                        link_li.insertAt(idx_,arr[i][z])
                else:
                    idx_ += 1
                    link_li.insertAt(idx_, arr[i][z])
    result = []
    link_li.listinput()
    print('#{}'.format(tc),end=' ')
    for i in range(-1,-11,-1):
        if i == -10:
            print(result[i])
        else:
            print(result[i],end=' ')