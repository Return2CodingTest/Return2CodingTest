# 338. Counting Bits

from typing import List

def countBits(n: int) -> List[int]:
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans


def countBits2(n: int) -> List[int]:
    ans = [0]
    def plusOneAtAllItemsInList(li):
        return [x+1 for x in li]

    while len(ans) < n+1:
        ans = ans[:] + plusOneAtAllItemsInList(ans[:])

    return ans[:n+1]

print(countBits2(8))