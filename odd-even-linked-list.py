class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        first = odd
        part = even
        pointer = head
        x = 1
        while pointer:
            if x % 2 == 1:
                odd.next = pointer
                odd = odd.next
            else:
                even.next = pointer
                even = even.next
            x += 1
            pointer = pointer.next
        odd.next = part.next
        even.next = None
