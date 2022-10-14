from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
    headHead = ListNode(0, head)
    cursor = head
    delayedCursor = headHead

    # Move cursor n - 1 steps forward
    for _ in range(n - 1):
      cursor = cursor.next

    # Move cursor and delayedCursor together
    while cursor.next:
      cursor = cursor.next
      delayedCursor = delayedCursor.next

    # delayedCursor is the node before the one to be removed
    delayedCursor.next = delayedCursor.next.next

    return headHead.next
