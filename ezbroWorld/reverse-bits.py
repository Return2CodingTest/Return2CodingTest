class Solution:
    def reverseBits(self, n: int) -> int:
        tmpArr = []

        for i in range(0,32):
            if n & 1 : tmpArr.append('1')
            else : tmpArr.append('0')
            n = n >> 1
            
        result = 0
        tmp = 1
            
        for i in range(len(tmpArr)-1,-1,-1):
            if tmpArr[i] == '1' : 
                result += tmp
            tmp *= 2
            
        return result
