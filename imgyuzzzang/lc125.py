# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(filter(str.isalnum, s)).upper()
        n = len(cleanString)
        
        start, end = 0, n - 1
        
        return cleanString == cleanString[::-1]
        