class linkedlist:
    def __init__(self):
        self.head=None
    def InsertAtMiddle(self,middle_Node,data):
        if middle_Node is None:
            print("the mentioned Node is absent")
            return
        temp=Node(data)
        temp.next=middle_Node.next
        middle_Node.next=temp
    def printlist(self):
        printt=self.head
        while printt is not None:
            print(printt.data,"==>",end='')
            printt=printt.next
        print("None")
    
list=linkedlist()
list.head=Node("mon")
e2=Node("tues")
e3=Node("wed")
list.head.next=e2
e2.next=e3
list.InsertAtMiddle(list.head.next,"thu")
list.printlist()
 
    
