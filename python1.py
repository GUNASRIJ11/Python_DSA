class Node:
    def __init__(self, data):

       
        self.prev = None
        self.data = data
        self.next = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_atfirst(self,data):
        
        newnode = Node(data)

        if self.head ==None:
            self.head =newnode
            self.tail =newnode
        else:

            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def delete_element(self,element):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp!=None:
                if temp.data == element:
                  
                    temp.prev.next = temp.next
                temp= temp.next

    def print_list(self):
        if self.head ==None:
            return 
        temp = self.head
        while temp!=None:
            print(temp.data, end=" ")
            temp =temp.next
        print()
        
    

         
    
list1 = Doublylinkedlist()
list1.insert_atfirst(1)
list1.insert_atfirst(2)
list1.insert_atfirst(3)
list1.insert_atfirst(4)
list1.insert_atfirst(5)
list1.insert_atfirst(6)
list1.insert_atfirst(7)
list1.insert_atfirst(8)
list1.print_list()
list1.delete_element(5)

list1.print_list()