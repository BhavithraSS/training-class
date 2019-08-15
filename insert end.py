class Node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class LL:
    def __init__(self):
        self.head=None
    def InsertAtEnd (self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
            return
        last=self.head
        while(last.nextt):
            last=last.nextt
        last.nextt=temp
    def printlist(self):
        printt=self.head
        while printt is not None:
            print(printt.data,"==>",end='')
            printt=printt.nextt
        print("None")
    
list=LL()
list.head=Node("mon")
e2=Node("tue")
e3=Node("wed")
list.head.nextt=e2
e2.nextt=e3
list.InsertAtEnd("thu")
list.printlist()
 
            
        
        
