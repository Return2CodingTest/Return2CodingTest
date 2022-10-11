# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # result = False
        # nodeSet = set()
        # while head :
        #     if head.next == None : 
        #         result = False
        #         break
        #     else :
        #         if head.val in nodeSet :
        #             result = True
        #             break
        #         nodeSet.add(head.val)
        #         head=head.next
        # return result
        # [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5] 이게 안됨

        nodeSet= set()
        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head= head.next
        return False

        
        # if head==None:
        #     return False
        # if head.next==None:
        #     return False
        # slow=head
        # fast=head
        # while fast!=None and fast.next!=None:
        #     fast=fast.next.next
        #     slow=slow.next
        #     if slow==fast:
        #         return True
        # return False
