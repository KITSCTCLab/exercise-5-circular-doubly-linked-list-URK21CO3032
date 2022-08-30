class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DLL:
    def __init__ (self):
        self.head=None

    def FrontInsert(self,data):
        if self.head is None:
            node=Node(data,self.head,None)
            self.head=node
            return
        else:
            node=Node(data,self.head,None)
            self.head.prev=node
            self.head=node

    def display(self):
        if self.head is None:
            print("linked list is empty.......")
            return
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("none")

n1=DLL()
n1.FrontInsert(10)
n1.FrontInsert(20)
n1.FrontInsert(13)
n1.FrontInsert(15)

n1.display()

