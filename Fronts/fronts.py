# Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.

class SLL:
    def __init__(self):
        self.head = None
    
    def front(self):
        if self.head is not None:
            return self.head.value
        else:
            return None

# Write a method to remove the head node and return the new list head node. If the list is empty, return null.

class sll:
    def __init__(self):
        self.head = None
    
    def removeFront(self):
        if self.head is not None:
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            return self.head
        else:
            return None

# Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SlL:
    def __init__(self):
        self.head = None
    
    def addFront(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self
        else:
            new_node.next=self.head
            self.head = new_node
        return self.head
# Write a method that accepts a value and create a new node, assign it to the end of the list
class Node:
    def __init__(self,val):
        self.name = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def addToBAck(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self