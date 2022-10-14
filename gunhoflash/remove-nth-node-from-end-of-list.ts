class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function removeNthFromEnd(head: ListNode, n: number): ListNode | null {
  const headHead = new ListNode(0, head);
  let cursor = head;
  let delayedCursor = headHead;

  // Move cursor n - 1 steps forward
  while (--n) cursor = cursor.next!;

  // Move cursor and delayedCursor together
  while (cursor.next) {
    cursor = cursor.next;
    delayedCursor = delayedCursor.next!;
  }

  // delayedCursor is the node before the one to be removed
  delayedCursor.next = delayedCursor.next!.next;

  return headHead.next;
}
