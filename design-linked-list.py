class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        n = self.head
        x = 0
        if not n:
            return -1
        else:
            while x != index:
                if not n.next:
                    return -1
                n = n.next
                x += 1
            return n.val
  

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        n = self.head
        new_node = Node(val)
        if not n:
            self.head = new_node
        else:
            while n.next:
                n = n.next
            n.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        n = self.head
        x = 0
        if x == index:
            new_node.next = n
            self.head = new_node
            return
            
        while x != index -1:
            if not n:
                return 
            n = n.next
            x += 1
 
        if n:
            new_node.next = n.next
            n.next = new_node
            


    def deleteAtIndex(self, index: int) -> None:
        n = self.head
        x = 0
        if x == index:
            self.head = n.next
            return

        while x != index -1:
            if not n.next:
                return
            n = n.next
            x += 1
      
        if n.next:
            n.next = n.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
