from typing import List

class Solution:
  def getHash(self, s: str):
    chars = list(s)
    chars.sort()
    return ''.join(chars)

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashMap = {}

    for s in strs:
      h = self.getHash(s)
      if not h in hashMap:
        hashMap.setdefault(h, [])
      hashMap.get(h).append(s)

    return hashMap.values()
