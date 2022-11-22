from collections import Counter

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    S = Counter(s)
    T = Counter(t)
    return S == T
