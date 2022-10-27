/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
const reorderList = function (head) {
  const paths = [];
  let res = new ListNode(0, null);
  const resStart = new ListNode(0, res);

  while (head) {
    const temp = head.next;
    head.next = null;
    paths.push(head);
    head = temp;
  }

  let start = 0;
  let end = paths.length - 1;

  while (start <= end) {
    res.next = paths[start];
    res = res.next;

    if (start !== end) {
      res.next = paths[end];
      res = res.next;
    }
    start += 1;
    end -= 1;
  }

  return resStart.next.next;
};
