# 190. Reverse Bits

from typing import List

def reverseBits(n: int) -> int:
    binary = format(n, "032b")
    return int(binary[::-1], 2)

print(reverseBits(43261596))