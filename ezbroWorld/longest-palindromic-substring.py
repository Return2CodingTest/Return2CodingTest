class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expend(s, left, right) : 
            while (0<=left) and (right<len(s)) and (s[left]== s[right]) : 
                left -= 1
                right += 1
            return s[left+1:right]
        
        max_palindrom = ""
        for i in range(len(s)) : 
            sub = expend(s,i,i)
            
            if len(sub) > len(max_palindrom) :
                max_palindrom = sub
                
            sub = expend(s,i, i+1)
            if len(sub) > len(max_palindrom) : 
                max_palindrom = sub
                
        return max_palindrom
