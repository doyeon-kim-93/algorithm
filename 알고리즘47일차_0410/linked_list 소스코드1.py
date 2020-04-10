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
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            self.tail = newnode
            self.cnt += 1

    def insertAt(self,idx,data):
        newnode = Node(data)
        if self.head is None or idx == 0:
            self.insertfirst(data)
        elif idx > self.cnt:
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

# <---------------------------delete---------------------------->
    def deleteFirst(self):
        if self.head == 0:
            print('empty')
            return
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.cnt -= 1

    def deleteLast(self):
        if self.head == 0:
            print('empty')
            return
        else:
            pre = None
            temp = self.head
            while temp.next != None:
                pre = temp
                temp = temp.next
            if pre is None:
                self.head = self.tail = None
            else:
                self.tail = pre
                pre.next = None
            self.cnt -= 1

    def deleteAt(self,idx):
        if self.head == 0:
            print('empty')
            return
        elif idx < 0 or idx > self.cnt :
            print('Index Error')
        else:
            pre = None
            temp = self.head
            for _ in range(idx):
                pre = temp
                temp = temp.next
            if pre is None:
                self.deleteFirst()
            elif temp == self.tail:
                self.deleteLast()
            else:
                pre.next = temp.next
            self.cnt -= 1

# <---------------------------print---------------------------->
    def print_List(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while temp != None:
                if temp == self.tail:
                    print(temp.data)
                else:
                    print(temp.data,end=' ')
                temp = temp.next

    def print_reverse(self, idx):
        if self.head == None:
            print('empty')
        else:
            pre = None
            temp = self.head
            while temp != self.tail:
                pre = temp
                temp = temp.next
            for _ in range(idx):
                print(temp.data, end=' ')
                temp = pre
                pre = temp.pre

    def print_lenth(self):
        if self.cnt == 0:
            print(0)
        else:
            print(self.cnt)

#<----------------------------etc------------------------->
    def listinput(self):
        global templist
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while temp != None:
                templist += [temp.data]
                temp = temp.next

    def Serch(self,data):
        newnode = Node(data)
        temp = self.head
        idx = 0
        while newnode.data > temp.data:
            idx += 1
            temp = temp.next
        return idx





list = Linkedlist()
for i in range(10):
    # list.insertfirst(i)
    list.insertLast(i)
# list.print_List()
# print(list.Serch(5))
# list.deleteFirst()
# templist = []
# list.listinput()
list.print_List()
list.print_reverse(5)
# print(templist)

