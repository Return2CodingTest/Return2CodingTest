class Solution:
    def hammingWeight(self, n: int) -> int:
        a = n
        cnt = 0
        while a > 0:
            cnt = cnt+1 if a % 2 != 0 else cnt
            a = a // 2
        return cnt
