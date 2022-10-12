#23. Merge k Sorted Lists

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    res = ListNode(0, None)
    resStart = None
    
    def getMinVal(ListNodes):
        minVal = 100
        minNode = None
        minIndex = 0

        for i, node in enumerate(ListNodes):
            if node and node.val < minVal:
                minNode = node
                minIndex = i
                minVal = node.val
        return (minNode, minIndex)

    while True:
        minNode, i = getMinVal(lists)
        res.next = minNode

        if resStart == None: resStart = res.next
        if minNode == None: return resStart

        lists[i] = lists[i].next
        res = res.next