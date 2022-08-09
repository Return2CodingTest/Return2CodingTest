class Solution:
  def getSum(self, a: int, b: int) -> int:
    _and = ((a & b) << 1) & 0x0ffffffff
    _xor = (a ^ b) & 0x0ffffffff
    result = (self.getSum(_xor, _and) if _and else _xor)

    return result if result <= 0x7fffffff else ~(result ^ 0xffffffff)
