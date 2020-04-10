class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def insertLast(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head =  newnode
            newnode.next = newnode
            newnode.pre = newnode
            self.cnt += 1
        else:
            temp = self.head
            con = 1
            while con is not self.cnt:
                temp = temp.next
                con += 1
            newnode.pre = temp
            temp.next = newnode
            self.tail = newnode
            self.head.pre = newnode
            newnode.next = self.head
            self.cnt += 1

    def insertAt(self,m,t):
        temp = self.head
        pre = temp.pre
        idx = 0
        start_idx = 0
        for _ in range(t):
            while idx-start_idx != m:
                pre = temp
                temp = temp.next
                idx += 1
            data = temp.pre.data + temp.data
            newnode = Node(data)
            temp.pre = newnode
            pre.next = newnode
            newnode.pre = pre
            newnode.next = temp
            temp = newnode
            start_idx += m
            self.cnt += 1

    def print_List(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            con = 0
            while con != self.cnt:
                print(temp.data,end=' ')
                temp = temp.next
                con += 1
        print()

    def print_lenth(self):
        if self.cnt == 0:
            return 0
        else:
            return self.cnt

    def listinput(self):
        global result
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            con = 0
            while con != self.cnt:
                result.append(temp.data)
                temp = temp.next
                con += 1

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = list(map(int,input().split()))
    li = Linkedlist()
    for i in range(N):
        li.insertLast(arr[i])
    li.insertAt(M,K)
    lens = li.print_lenth()
    result = []
    li.listinput()
    print('#{}'.format(tc), end=' ')
    if lens < 10:
        print(*result[-1::-1])
    else:
        print(*result[-1:-11:-1])


