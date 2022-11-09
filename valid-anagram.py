from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterT = Counter(t)
        for c in s :
            counterT[c] -=1
        
        for key in counterT :
            if counterT[key] != 0 :
                return False
        return True
