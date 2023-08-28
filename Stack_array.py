

# # string reverse using stack

# # from collections import deque


# def stack_size():
    

# # str1 = 'hi this is gunasri'
# # lst= str1.split()
# # stack =deque()
# # top =-1
# # for i in lst:
# #     stack.append(i)
# #     top+=1
# # print(top)   
# # print(stack)


# # popped_items = []
# # while stack:
# #     popped_items.append(stack.pop())
# #     top -= 1

# # print(top)
# # print(popped_items)


# from collections import deque

# class Stack:
    
#     def __init__(self):
#         self.stack = deque()
#         self.Top = -1

#     def push(self, item):
#         self.stack.append(item)
#         self.Top+=1

#     def pop(self):
#         if self.is_empty():
#             return "the stack is empty"
#         self.Top-=1
#         return self.stack.pop()

#     def is_empty(self):
#         return self.Top==-1

#     def size(self):
#         return self.Top+1

#     def top(self):
#         if self.is_empty():
#             return"Stack is empty"
#         return self.stack[self.Top]


# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.pop())  # Output: 30
# print(stack.top())  # Output: 20
# print(stack.size())  # Output: 2
# print(stack.is_empty())  # Output: False


# ------------------------------------------------------------------------


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []
    

    def push(self,data):
        if self.top == -1:
            self.stack.append(data)
            self.top = 0
        else:
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if self.top==-1:
            print("the stack is empty")
        else:
            self.top-=1


    def printstack(self):
        temp = self.top
        while self.top>=0:
            print(self.stack[self.top], end=" ") 
            self.top-=1

    def is_empty(self):
        if self.top==-1:
           print("true")
        else:
         print("false")


    def size(self):
        print(self.top+1)
            
    


stack1 = Stack()
stack1.is_empty()
stack1.push(20)
stack1.push(20)
stack1.push(20)
stack1.push(20)
stack1.push(20)
stack1.push(20)
stack1.push(1111111111)
stack1.size()
stack1.printstack()


