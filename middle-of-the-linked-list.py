class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        left, right = head, head

        if not head:
            return None

        while right and right.next:
            right = right.next.next
            left = left.next
            head = head.next.next
        
        dummy.next = left
        return dummy.next
