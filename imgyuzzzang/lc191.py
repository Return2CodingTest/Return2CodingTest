# 191. Number of 1 Bits

from typing import List

def hammingWeight(n: int) -> int:
    binary_n = bin(n)
    return binary_n.count('1')