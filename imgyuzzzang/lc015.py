#15. 3Sum
from typing import List
from itertools import combinations

def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    combs = list(combinations(nums, 3))
    visitedSet = []
    for comb in combs:
        a, b, c = comb
        if a + b + c == 0:
            if set(comb) in visitedSet:
                continue
            visitedSet.append(set(comb))
            res.append([a,b,c])
    return res

print(threeSum([-1,0,1,2,-1,-4]))

