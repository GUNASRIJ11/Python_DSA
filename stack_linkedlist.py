# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = -1
        

#     def push(self, item):
#         new_node = Node(item)
#         if self.top==-1:
#             self.top+=1
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#             self.top+=1
        

#     def pop(self):
#         if self.top ==-1:
#             return "Stack is empty"
#         popped_item = self.top.data
#         self.top = self.top.next
#         self.top-=1
        
#         return popped_item

#     def is_empty(self):
#         return  self.top ==-1

#     def get_size(self):
#         return self.top + 1

#     def peek(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.top.data



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        if self.top ==None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top==None:
            return "Stack is empty"
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item

    def is_empty(self):
        return not self.top

    def get_size(self):
        size = 0
        current = self.top
        while current:
            size += 1
            current = current.next
        return size

    def peek(self):
        if not self.top:
            return "Stack is empty"
        return self.top.data
    
    def display(self):
        if self.top ==None:
            return "Stack is empty"
        else:
            temp = self.top
            while temp.next!= None:
                print(temp.data)
                temp = temp.next
            print(temp.data)



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.get_size())  # Output: 2
print(stack.is_empty())  # Output: False
stack.display()





