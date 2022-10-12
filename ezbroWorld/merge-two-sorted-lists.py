import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        heapedList = list()
        head = ListNode(-1)
        cursor = head

        while list1:
            heapq.heappush(heapedList,list1.val)
            list1 = list1.next

        while list2:
            heapq.heappush(heapedList,list2.val)
            list2 = list2.next

        length = len(heapedList)

        for i in range(length) :
            cursor.next = ListNode(heapq.heappop(heapedList))
            cursor = cursor.next
        
        return head.next
