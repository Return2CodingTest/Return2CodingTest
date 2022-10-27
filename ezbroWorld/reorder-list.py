from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dq = deque()
        node = head
        while node : 
            dq.append(node.val)
            node = node.next
        size = len(dq)
        
        for i in range(size) : 
            if i%2 == 0 : 
                head.val = dq.popleft()
                head = head.next
            else :
                head.val = dq.pop()
                head = head.next
