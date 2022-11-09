from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=end=0 
        length = len(s)
        counter = Counter()
        
        for end in range(1,length+1) : 
            counter[s[end-1]]+=1
            
            frequentCnt = counter.most_common(1)[0][1]
            
            if end-start-frequentCnt > k : 
                counter[s[start]]-=1
                start+=1
                
        return end- start
