class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        output = temp
        left = list1
        right = list2

        while left and right:
            if left.val < right.val:
                output.next = left
                left = left.next
            else:
                output.next = right
                right = right.next
                
            output = output.next
        
        if left:
            output.next = left
        else:
            output.next = right

        return temp.next
