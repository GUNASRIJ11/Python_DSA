class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)

    def count_nodes(self):
        count = 0
        if self.head is None:
            return 0
        else:
            temp = self.head
            while temp.next is not None:
                count += 1
                temp = temp.next
            return count + 1

    def push_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_end(self, data):
        
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def push_middle(self, middle_node, data):
        if middle_node is None:
            print("There is no such middle node")
            return
        new_node = Node(data)
        new_node.next = middle_node.next
        new_node.prev = middle_node
        if middle_node.next is not None:
            middle_node.next.prev = new_node
        middle_node.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("There is no linked list")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

    def add_node(self, pos, data):
        position = pos
        count = 0
        new_node = Node(data)
        temp = self.head
        while count < position - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    def reverse_linked_list(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

    def remove_duplicates(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
                if current.next is not None:
                    current.next.prev = current
            else:
                current = current.next


list1 = DoublyLinkedList()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(40)
node6 = Node(60)
node7 = Node(60)

list1.head = node1
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5
node6.next = node7
node7.prev = node6


DoublyLinkedList.print_list(list1)
DoublyLinkedList.remove_duplicates(list1)
DoublyLinkedList.print_list(list1)









# -------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head  = None
        self.tail = None
    

    def push_begin(self,data):
        new_node = Node()
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node




    def push_end(self, data):
        new_node = Node()
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def push_position(self, data, pos):
        new_node = Node(data)
        if self.head == None:
           print("list is empty")
        else:

            temp = self.head
            count = 0
            while(count<pos):
                count+=1
                tem = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
            

    def 




   






