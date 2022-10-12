#141. Linked List Cycle

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def hasCycle(head: Optional[ListNode]) -> bool:
    visited = set()
    while True:
        if not head or head.next == None:
            return False
        if head in visited:
            return True
        visited.add(head)
        head = head.next