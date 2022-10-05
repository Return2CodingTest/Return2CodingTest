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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (lists === null) return null;

  const len = lists.length;
  if (len === 0) return null;
  if (len === 1) return lists[0];
  if (len === 2) return mergeTwoLists(lists[0], lists[1]);
  return mergeTwoLists(
    mergeKLists(lists.slice(0, len / 2)),
    mergeKLists(lists.slice(len / 2))
  );
}
