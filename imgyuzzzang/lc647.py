# 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        def getExpendPalindromeCount(start, end):
            count = 0
            while start >= 0 and end  < n and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
            return count
        
        for start in range(n):
            ans += getExpendPalindromeCount(start, start)
            ans += getExpendPalindromeCount(start, start + 1)
        
        return ans