#creates class for Node
class Node:
    def __init__(self, month=None):
        self.month=month
        self.next_month=None

#creates class for linked list            
class linkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        printed = self.head
        while printed is not None:
            print(printed.month)
            printed = printed.next

month_list = linkedList()
month_list.head = Node("January")
n2 = Node("february")
n3 = Node("March")
n4 = Node("April")
n5 = Node("May")
n6 = Node("June")
n7 = Node("July")
n8 = Node("August")
n9 = Node("September")
n10 = Node("October")
n11 = Node("November")
n12 = Node("December")
 
month_list.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n12

month_list.printlist()
