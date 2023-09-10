class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = self.k
        self.head = ListNode(0)
        self.tail = self.head

        

    def enQueue(self, value: int) -> bool:
        new = ListNode(value)

        if self.size == 0:
            return False
        else:
            self.size -= 1

        self.tail.next = new
        self.tail = new
        return True


    def deQueue(self) -> bool:
        if self.size ==  self.k:
            return False
        else:
            self.size += 1

            if self.head.next:
                temp = self.head.next
                self.head.next = temp.next
                temp.next = None

            if not self.head.next:
                self.tail = self.head
            return True

        

    def Front(self) -> int:
        if self.head.next:
            return self.head.next.val
        else:
            return -1

        

    def Rear(self) -> int:
        if self.size == self.k:
            return -1
        else:
            return self.tail.val

        

    def isEmpty(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False


        

    def isFull(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
