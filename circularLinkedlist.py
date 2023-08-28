# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

    
#     def add_element(self, data):
#         new_node = node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node


#     def printlist(self):
#         if self.head ==None:
#             return 
#         temp =self.head
#         while(temp.next!=None):
#             print(temp.data, end=" ")
#             temp = temp.next
#             if temp.next == self.head:
#                 break
#         print(temp.data)
        


# list1 = Linkedlist()
# node1 = node(10)
# node2 = node(20)
# node3 = node(30)
# node4 = node(40)
# node5 = node(50)
# node6 = node(60)
# node7 = node(70)

# list1.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7
# node7.next = list1.head

# result  = Linkedlist.printlist(list1)



# -----------------------------------------------------------------------------------------




class node:
    def __init__(self,data):
        self.data=data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    

    def addbegin(self,data):
        newnode = node(data)
        if self.head ==None:
            self.head = newnode
            
            self.tail = newnode
            self.next = self.head

        else:
            newnode.next = self.head
            self.head = newnode



    def addend(self, data):
        newnode =node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            self.next = self.head
        else:
            self.tail.next=newnode
            self.tail = newnode
            self.tail.next  = self.head

    def delbegin(self):
        if self.head==None:
            return 
        else:
            self.head =self.head.next
            self.tail.next = self.head 

    def delend(self):
       def delend(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp

             

            
    




            

    

    def display(self):
        
        if self.head ==None:
            return 
        temp =self.head
        while(temp.next!=None):
            print(temp.data, end=" ")
            temp = temp.next
            if temp.next == self.head:
                break
        print(temp.data)
        
    
list1 = Linkedlist()
list1.addbegin(10)
list1.addbegin(20)
list1.addbegin(30)
list1.addbegin(30)
list1.addbegin(40)
list1.addbegin(50)
list1.addend(2)
list1.addend(3)
list1.addend(4)
list1.addend(5)
list1.addend(4)
list1.addend(5)
list1.display()
list1.delbegin()
list1.display()
list1.delend()
list1.display()