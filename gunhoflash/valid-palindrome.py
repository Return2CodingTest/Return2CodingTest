import re

class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = re.sub(r'[^0-9A-Za-z]', '', s).lower()
    length = len(s)
    half = (length + 1) // 2
    for i in range(half):
      if s[i] != s[length - 1 - i]:
        return False
    return True
