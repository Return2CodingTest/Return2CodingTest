class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        characterToIndex = {}
        startIndex = 0
        maxLength = 0
        for i in range(n):
            character = s[i]
            if character in characterToIndex and characterToIndex[character] >= startIndex:
                if maxLength < i - startIndex:
                    maxLength = i - startIndex
                startIndex = characterToIndex[character] + 1
                
                if n - startIndex < maxLength:
                    break
            
            characterToIndex[character] = i
        
        if n - startIndex > maxLength:
            maxLength = n - startIndex
        
        return maxLength