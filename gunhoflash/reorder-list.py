from collections import deque
from typing import List, Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    deq = deque()
    while head:
      deq.append(head)
      head = head.next

    tail = deq.popleft()
    while True:
      if deq:
        tail.next = deq.pop()
        tail = tail.next
      else:
        break
      if deq:
        tail.next = deq.popleft()
        tail = tail.next
      else:
        break
    tail.next = None
