const removeNthFromEnd = function (head, n) {
  const start = new ListNode(0, null);
  start.next = head;
  let count = 1;
  let totalLength = 0;

  while (head) {
    head = head?.next;
    totalLength += 1;
  }

  head = start.next;

  const nth = totalLength - n + 1;

  if (nth === 1) {
    return head.next;
  }

  while (count !== nth - 1) {
    head = head?.next;
    count += 1;
  }

  head.next = head?.next?.next || null;

  return start.next;
};
