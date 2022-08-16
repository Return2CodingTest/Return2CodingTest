class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0 : return [0]
        elif n == 1 : return [0,1]
        
        result = []
        result.append(0)
        result.append(1)
        tmp = 0
        for i in range(2,n+1):
            if i & (i-1) == 0 : 
                tmp = i
            result.append(result[tmp ^ i] + 1)
            
        return result
