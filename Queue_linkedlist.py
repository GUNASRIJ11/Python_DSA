# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
    
#     def enqueue(self, data):
#         new_node = node(data)
#         if self.rear == None:
#             self.front = new_node
#             self.rear = new_node
        
#         else:
#             new_node.next = self.rear
#             self.rear = new_node

#     def dequeue(self):
#         if self.rear ==None:
#             return "the queue is empty"
#         self.rear = self.rear.next
        

#     def print_list(self):
#         if self.front is None:
#             print("The queue is empty")
#         else:
#             temp = self.front
#             while temp is not None:
#                 print(temp.data)
#                 temp = temp.next





# queue = Queue()
# node1 = node(10)
# node2 = node(20)
# node3 = node(30)
# node4 = node(40)

# node5 = node(40)
# node6 = node(60)
# node7 = node(60)
# Queue.enqueue(queue,node1)
# Queue.enqueue(queue,node2)
# Queue.enqueue(queue,node3)
# Queue.enqueue(queue,node4)
# Queue.enqueue(queue,node5)
# Queue.enqueue(queue,node6)
# Queue.enqueue(queue,node7)


# Queue.print_list(queue)

# # queue1 = Queue()
# # Queue.print_list(queue1)





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "The queue is empty"
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next



    def display(self):
        if self.front is None:
            print("The queue is empty")
        else:
            temp = self.front
            while temp.next!=None:
                print(temp.data, end = "->")
                temp = temp.next
            print(temp.data)



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.display()  
queue.dequeue()
queue.display()  
