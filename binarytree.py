class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def print_tree(root):
    if root is None:
        return 
    
    print(root.data, end=":")
    if root.left is not None:
        print('L', root.left.data, end=",")
    if root.right is not None:
        print('R', root.right.data, end=",")
    print()

    print_tree(root.left)
    print_tree(root.right)




def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
   


def preorder(root):
    if root:
        print(root.data, end =" ")
        preorder(root.left)
        preorder(root.right)




def postorder(root):
    if root:
        
        postorder(root.left)
        postorder(root.right)
        print(root.data, end =" ")
        
        



def tree_input():
    global count
    root_data = int(input())

    if root_data == -1:
        return None
    
    
    root = Node(root_data)
    count+=1
    left = tree_input()
    right = tree_input()
    root.left = left
    root.right = right  

    return root     

count = 0
root = tree_input()
print_tree(root)



print("no. of nodes:",count)



inorder(root)
print()
preorder(root)
print()
postorder(root)


    



    