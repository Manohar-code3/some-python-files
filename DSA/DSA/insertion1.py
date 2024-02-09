class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linked:
    def __init__(self):
        self.headval=None
    def print_val(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
L1=Linked()
L1.headval=node("1")
e2=node("2")
e3=node("3")
L1.headval.nextval=e2
e2.nextval=e3
L1.print_val()