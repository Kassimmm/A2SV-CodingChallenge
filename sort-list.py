# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(arr1, arr2):
            temp = ListNode()
            res = temp
            while arr1 and arr2:
                if arr1.val < arr2.val:
                    temp.next = arr1
                    arr1 = arr1.next
                else:
                    temp.next = arr2
                    arr2 = arr2.next
                temp = temp.next
            temp.next = arr1 or arr2
            return res.next

        if not head or not head.next:
            return head

        left = start = right = ListNode(0, head)
        while right and right.next:
            right = right.next.next
            left = left.next
        end = left.next
        left.next = None
        return merge(self.sortList(start.next), self.sortList(end))
        
