from collections import Counter

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    S = Counter(s)
    T = Counter(t)
    return len(S - T) == 0 and len(T - S) == 0
