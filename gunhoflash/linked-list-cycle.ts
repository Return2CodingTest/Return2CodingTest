class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function hasCycle(head: ListNode | null): boolean {
  let p1 = head, p2 = head;
  while (p2 && p2.next) {
    p1 = p1!.next;
    p2 = p2.next.next;
    if (p1 === p2) return true;
  }
  return false;
}
