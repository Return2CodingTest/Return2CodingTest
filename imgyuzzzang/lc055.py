# 55. Jump Game

from typing import List

def canJump(nums: List[int]) -> bool:
    n = len(nums)
    jumpable = [0] * n
    jumpable[0] = 1
    
    def setJumpable(m):
        while(m):
            if jumpable[m] == 1:
                return 0
            jumpable[m] = 1
            m -= 1
            
    for i in range(n):
        if jumpable[i] == 1:
            next = min(i+nums[i], n-1)

            if next == n-1:
                return True
            setJumpable(next)
    return False