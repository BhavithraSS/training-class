class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def InsertAtBeg(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp 
    
    def printList(self):
        printt=self.head
        while printt is not None:
            print(printt.data,"==>",end='')
            printt=printt.next
        print("None")
list=linkedlist()
list.head=Node("mon")
e2=Node("tue")
e3=Node("wed")
list.head.next=e2
e2.next=e3
list.InsertAtBeg("thu")
list.printList()
 
