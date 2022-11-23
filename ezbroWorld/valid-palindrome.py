class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = s
        newS = list(filter(str.isalnum, newS))
        newS = ''.join(newS).lower()
        print(newS)
        
        l = len(newS)
        if l == 1 : return True
        if len(newS) % 2 == 0 :
            #012345
            if newS[0:l//2] == newS[l-1:(l//2)-1:-1] :
                return True
            return False
        else :
            #01234
            if newS[0:(l//2)] == newS[l-1:(l//2):-1] :
                return True
            return False
