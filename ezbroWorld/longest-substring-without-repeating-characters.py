class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        subStr = ""
        for i in range(len(s)) : 
            if s[i] in subStr : 
                subStr = subStr[subStr.index(s[i])+1:]
                
            subStr += s[i]
            maxLength = max(maxLength, len(subStr))
            
        return maxLength
