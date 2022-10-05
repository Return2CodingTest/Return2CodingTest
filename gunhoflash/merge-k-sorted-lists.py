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

  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if lists is None: return None

    length = len(lists)
    if length == 0: return None
    if length == 1: return lists[0]
    if length == 2: return self.mergeTwoLists(lists[0], lists[1])
    return self.mergeTwoLists(
      self.mergeKLists(lists[ : length >> 1]),
      self.mergeKLists(lists[length >> 1 : ])
    )
