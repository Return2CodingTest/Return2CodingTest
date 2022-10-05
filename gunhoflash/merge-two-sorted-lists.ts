class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  const head = new ListNode();
  let tail = head;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      tail = tail.next = list1;
      list1 = list1.next;
    } else {
      tail = tail.next = list2;
      list2 = list2.next;
    }
  }

  tail.next = list1 || list2;

  return head.next;
}
