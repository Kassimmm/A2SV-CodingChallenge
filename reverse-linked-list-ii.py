class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = dummy.next

        for i in range(left-1):
            prev = prev.next

        curr = prev.next
        for i in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            prev.next = temp

        return dummy.next
