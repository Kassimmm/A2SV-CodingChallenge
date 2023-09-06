class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            has_duplicates = False
            while current.next and current.val == current.next.val:
                current = current.next
                has_duplicates = True
            if has_duplicates:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next
