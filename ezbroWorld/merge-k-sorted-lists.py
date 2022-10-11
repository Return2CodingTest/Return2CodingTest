import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heapedList = list()
        resultLinkedList = ListNode(-1)
        cursor = resultLinkedList

        for i in range(len(lists)) : 
            head = lists[i]
            while head : 
                heapedList.append(head.val)
                head = head.next
        
        heapq.heapify(heapedList)
        length = len(heapedList)

        for i in range(length) : 
            cursor.next = ListNode(heapq.heappop(heapedList))
            cursor = cursor.next
        
        return resultLinkedList.next
