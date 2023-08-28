

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


