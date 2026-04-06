class person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello" , self.name)

p1 = person("Moti")
p1.greet()

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def addAtTail(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def addAtBegining(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
 
        new_node.next = self.head
        self.head = new_node
    
    def addAtCertainPos(self, val, pos):
        new_node = Node(val)
        current = self.head

        count_pos = 2
        while current.next and count_pos < pos:
            current = current.next
            count_pos += 1
        new_node.next = current.next
        current.next = new_node
    
    def printList(self):
        current = self.head
        while current:
            print(current.val, end="->")
            current = current.next
        print("None")

ll = MyLinkedList()
ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
ll.addAtBegining(0)
ll.addAtCertainPos(100,3)
ll.printList()


