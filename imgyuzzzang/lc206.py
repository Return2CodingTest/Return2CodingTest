#206. Reverse Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
    nextNode = prevNode = None  
    
    while head:
        nextNode = head.next
        head.next = prevNode
        prevNode = head
        
        print(head.val)
        
        head = nextNode
        
    return prevNode