class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function reorderList(head: ListNode | null): void {
  const deq: ListNode[] = [];
  while (head) {
    deq.push(head);
    head = head.next;
  }

  let tail = deq.shift()!;
  while (true) {
    tail.next = deq.pop() || null;
    if (tail.next === null) return;
    tail = tail.next;
    tail.next = deq.shift() || null;
    if (tail.next === null) return;
    tail = tail.next;
  }
}
