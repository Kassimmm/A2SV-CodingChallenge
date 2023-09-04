class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target = head

        while target:
            while target.next and target.next.val == target.val:
                target.next = target.next.next
            target = target.next
        return head
