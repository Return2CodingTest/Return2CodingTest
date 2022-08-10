class Solution(object):
    def getSum(self, a, b):
        
        if b == 0:
            return a
        sum = a ^ b
        carry = (a & b) << 1
        return self.getSum(sum, carry)
    
    
    # a^b -> XOR연산 -> 해당 자리 값  
    # a&b -> AND연산 -> carry bit 값
    # (a&b) << 1 -> carry bit니깐 왼쪽으로 밀어줌
    
    # minus 는 처리하지 못함... python의 인트값이 무한이기 때문에...
