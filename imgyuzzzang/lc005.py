# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)
        
        def getExpendPalindrome(start, end):
            while start >= 0 and end  < n and s[start] == s[end]:
                start -= 1
                end += 1
                
            return s[start+1:end]
        
        for start in range(n):
            pal1 = getExpendPalindrome(start, start)
            pal2 = getExpendPalindrome(start, start + 1)
            _, ans = max((len(pal1), pal1), (len(pal2), pal2), (len(ans), ans))
        
        return ans