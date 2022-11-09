from collections import defaultdict
from queue import deque
class Solution:
    def isValid(self, s: str) -> bool:
        myD = defaultdict(list)
        myD["("].append("(")
        myD["("].append(")")
        myD["{"].append("{")
        myD["{"].append("}")
        myD["["].append("[")
        myD["["].append("]")
        left, right = ["[","{","("], ["]","}",")"]
        
        dQ = deque()
        
        for i in range(len(s)) :
            if s[i] in left :
                dQ.append(s[i])
            
            if s[i] in right :
                if len(dQ) == 0 : 
                    return False
                
                if myD[dQ.pop()][1] == s[i] : 
                    continue
                
                else : return False
                
        if len(dQ) != 0 : 
            return False
        return True
