class node():
    def __init__(self,data):
        self.data=data
        self.nxt=None
class sll():
    def __init__(self):
        self.head=None
    def insertion(self,data):
        tmp=node(data)
        tmp.nxt=self.head
        self.head=tmp
    def deletion(self,data):
        tmp=self.head
        self.head=self.head.nxt
        tmp.nxt=None
    def printlist(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.data,"==>",end='')
            tmp=tmp.nxt
        print("none")
list=sll()
list.head=node("tue")
e2=node("mon")
e3=node("wed")
list.head.nxt=e2
e2.nxt=e3
list.deletion("")
list.printlist()
