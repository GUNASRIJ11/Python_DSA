# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next = None


# class Linkedlist:
    
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def printlist(self):
        
#         if self.head ==None:
#             return 
#         temp =self.head
#         while(temp.next!=None):
            

#             print(temp.data, end=" ")
#             temp = temp.next
#         print(temp.data)

#     def count_node(self):
#         count=0
#         if self.head ==0:
#             return 0
#         else:
#             temp = self.head
#             while temp.next!=None:
#                 count+=1
#                 temp = temp.next
#             return count+1


#     def pushbegin(self, data):
#         if self.head ==None:
#             self.data = data
#         newnode = node(data)
#         newnode.next = self.head
#         self.head = newnode

#     def pushend(self, data):
#         if self.head == None:
#             self.data = data
#         newnode =node(data)
#         temp = self.head
#         while(temp.next!=None):
#             temp =temp.next
#         temp.next = newnode

#     def pushmiddle(self, middlenode, data):
#         if middlenode == None:
#             print("There is no such middelnode")
#         newnode = node(data)
#         newnode.next = middlenode.next
#         middlenode.next = newnode


#     # def reverse_list(self):
#     #     rest  = Linkedlist.reverse_list(self.head.next)
#     #     temp = rest
#     #     while(temp.next!=None):
#     #         temp = temp.next
#     #     temp.next = self.head
#     #     self.head.next = None

    

#     def delete_begin(self):
#         if self.head ==None:
#             print("there is no linkedlist")
#         self.head= self.head.next
        
       

#     # def delete_end(self):
#     #     if self.head == None:
#     #         print("there is no linkedlist")
#     #     temp = self.head
#     #     while temp.next!= None:
#     #         print(temp.data, end=" ")
#     #         temp = temp.next
#     #     print()


#     def delete_end(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return

#         if self.head.next is None:
#             self.head = None
#             return

#         temp = self.head
#         while temp.next.next is not None:
#             temp = temp.next
#         temp.next = None

#     def add_node(self,pos, data):
#         position  =pos
#         count =0
#         newnode = node(data)
#         temp = self.head
#         while(count<position-1):
#             temp = temp.next
#             count+=1
#         newnode.next = temp.next
#         temp.next = newnode






#     def reverse_linked_list(self):
#         prev = None
#         current = self.head

#         while current is not None:
#             next_node = current.next
#             current.next = prev


#             prev = current
#             current = next_node

#         return prev

    




#     def remove_duplicates(self):
#         curr = self.head
        
#         while curr!= None and curr.next !=None:

#             if curr.data ==curr.next.data:
#                 curr.next = curr.next.next
            
#             else :
#                 curr = curr.next
        







            



# list1 = Linkedlist()
# node1 = node(10)
# # node2 = node(20)
# # node3 = node(30)
# # node4 = node(40)

# # node5 = node(40)
# # node6 = node(60)
# # node7 = node(60)

# list1.head = node1
# # node1.next = node2
# # node2.next = node3
# # node3.next = node4
# # node4.next = node5
# # node5.next = node6
# # node6.next = node7


# Linkedlist.printlist(list1)
# list1.pushbegin(20)


# # Linkedlist.reverse_list(list1)
# # result  = Linkedlist.printlist(list1)


# # Linkedlist.add_node(list1, 2,45)
# # Linkedlist.printlist(list1)

# # Linkedlist.delete_begin(list1)
# # Linkedlist.printlist(list1)




# # Linkedlist.delete_end(list1)
# # Linkedlist.printlist(list1)




# Linkedlist.remove_duplicates(list1)
# Linkedlist.printlist(list1)







# # insert_at_end = Linkedlist.pushend(list1,1200)
# # result  = Linkedlist.printlist(list1)

# # Linkedlist.pushmiddle(list1,node3,16600)
# # result  = Linkedlist.printlist(list1)


# # reverse = Linkedlist.reverse_linked_list(list1)

# # current = reverse
# # while current is not None:
# #     print(current.data, end=" ")
# #     current = current.next



# ________________________________________________________________________________________________




class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_element(self, data):
        new_node =  Node(data)
        if self.head ==None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        
    def push_begin(self, data):
        newnode = Node(data)
        if self.head ==None:
            self.data = data
        newnode.next = self.head
        self.head = newnode



    def pushend(self, data):
        if self.head == None:
            self.data = data
        new_node =Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def push_position(self, middlenode, data):
        if middlenode == None:
            print("There is no such middelnode")
        newnode = Node(data)
        newnode.next = middlenode.next
        middlenode.next = newnode


    def add_node(self,position, data):
        
        count =0
        newnode = Node(data)
        temp = self.head
        while(count<position-1):
            temp = temp.next
            count+=1
        newnode.next = temp.next
        temp.next = newnode


    # def reverse_list(self):
    #     rest  = Linkedlist.reverse_list(self.head.next)
    #     temp = rest
    #     while(temp.next!=None):
    #         temp = temp.next
    #     temp.next = self.head
    #     self.head.next = None


    def reverse_linkedlist(self):
        if self.head==None:
            return None
        else:
            h = self.head
            t= self.tail
            i = 0
            while i < self.count_node():
                temp = h.data

                h.data = t.data
                t.data = temp
                h  = h.next
                t =  t.next
                i+=1
            return 
                






    def remove_duplicates_sortedlist(self):
        curr = self.head
        
        while curr!= None and curr.next !=None:

            if curr.data ==curr.next.data:
                curr.next = curr.next.next
            
            else :
                curr = curr.next



        





        

    def count_node(self):
        count=0
        if self.head ==0:
            return 0
        else:
            temp = self.head
            while temp!=None:
                count+=1
                temp = temp.next
            return count


    
    
    def display_list(self):
        if self.head ==None:
            return 'Linkedlist is empty'
        else:
            temp = self.head
            while temp!=None:
               print(temp.data, end=" ")
               temp = temp.next
            print()
           
           



list1 = Linkedlist()
list1.add_element(10)
list1.add_element(20)
list1.add_element(20)
list1.add_element(20)
list1.add_element(2200000)
list1.push_begin(200002222)
list1.display_list()
list1.count_node()
list1.reverse_linkedlist()
        


