class node():
    def __init__(self,data):
        self.data=data
        self.nxt=None
class linkedlist():
    def __init__(self):
        self.head=None
    def insertion(self,data):
        tmp=node(data)
        tmp.nxt=self.head
        self.head=tmp
    def deletionatend(self,data):
        tmp = self.head
        while(tmp.nxt is not None):
            prev  = tmp
            tmp = tmp.nxt
        prev.nxt = None

    def printlist(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.data,"==>",end='')
            tmp=tmp.nxt
        print("none")
list=linkedlist()
list.head=node("mon")
e2=node("tue")
e3=node("wed")
list.head.nxt=e2
e2.nxt=e3
list.deletionatend("")
list.printlist()
