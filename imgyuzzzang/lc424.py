class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charToIndex = {}
        res = 0
        n = len(s)
                
        def getMaxByAlphabet(alp):
            indeces =  charToIndex[alp]
            now = 0
            while now === len(indeces) :
        
        for i in range(n):
            alp = s[i]
            if alp in charToIndex:
                charToIndex[alp] = [i]
            else:
                charToIndex[alp].append(i)
        for alp in charToIndex:
            