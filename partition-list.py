class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        part1, part2 = left, right 

        while head:
            if head.val < x:
                part1.next = head
                part1 = part1.next
            else:
                part2.next = head
                part2 = part2.next
            head = head.next
        
        part1.next = right.next
        part2.next = None

        return left.next
