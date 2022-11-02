#21. Merge Two Sorted Lists

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
    
    nodeList = [list1, list2]

    while True:
        minNode, i = getMinVal(nodeList)
        res.next = minNode

        if resStart == None: resStart = res.next
        if minNode == None: return resStart
        
        nodeList[i] = nodeList[i].next
        res = res.next
            