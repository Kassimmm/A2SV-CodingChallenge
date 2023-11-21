class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merger(list1, list2):
            dummy = ListNode(0) 
            res = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next
            dummy.next = list1 or list2
            return res.next

        if len(lists) == 0:
             return None
        if len(lists) == 1:
            return lists[0]

        temp = merger(lists[0], lists[1])
        for i in range(2, len(lists)):
            temp = merger(temp, lists[i])
        return temp
