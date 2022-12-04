class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countPalinFromAxis(s,left, right) : 
            count = 0
            while (0 <= left) and (right < len(s)) and (s[left] == s[right]) :
                left -= 1
                right += 1
                count += 1
                
            return count
        totalCount = 0
        for i in range(len(s)) : 
            totalCount += countPalinFromAxis(s,i,i)
            totalCount += countPalinFromAxis(s,i,i+1)
            
        return totalCount
