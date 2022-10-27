# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=1
        node = head
        while node.next != None:
            size+=1
            node=node.next
        if size==1 :
            head.next=None
            return head.next
        if size==n :
            return head.next
        
        resultNode = head
        for i in range(size-n-1):
            resultNode = resultNode.next
        removeNext = resultNode.next.next
        resultNode.next = removeNext
    
        return head
