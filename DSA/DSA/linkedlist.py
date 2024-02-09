class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
    def print_the(self):
        printval=self.head
        while printval is not None:
            print(printval.dataval)
            printval=printval.next

L1=Linked()
L1.head=node("1")
l2=node("2")
l3=node("3")
L1.head.next=l2
l2.next=l3
L1.print_the()
        