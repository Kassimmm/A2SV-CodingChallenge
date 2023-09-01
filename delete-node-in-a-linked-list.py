class Solution:
    def deleteNode(self, node):
        target = node.next
        node.val = target.val
        node.next = target.next
