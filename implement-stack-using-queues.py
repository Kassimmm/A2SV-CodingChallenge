class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None


    def push(self, x: int) -> None: 
        new_node = ListNode(x)
        curr = self.head
        new_node.next = curr
        self.head = new_node
        

    def pop(self) -> int:
        curr = ans = self.head
        temp = curr.next
        curr.next = None
        curr = temp
        self.head = curr
        return ans.val
    

    def top(self) -> int:
        if not self.head:
            return None
        else:
            return self.head.val
        
   

    def empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
