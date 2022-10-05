from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    tail = head

    while list1 and list2:
      if list1.val < list2.val:
        tail.next = list1
        tail = list1
        list1 = list1.next
      else:
        tail.next = list2
        tail = list2
        list2 = list2.next

    tail.next = list1 or list2

    return head.next
