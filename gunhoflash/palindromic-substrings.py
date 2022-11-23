class Solution:
  def countSubstrings(self, s: str) -> int:
    count = 0

    L = len(s)
    LRDP = [[False] * L for _ in range(L)]

    def setLRDP(left: int, right: int, value: bool):
      nonlocal count
      if value is True:
        LRDP[left][right] = True
        count += 1

    # String(length=1) is always a palindrome
    setLRDP(0, 0, True)
    for right in range(1, L):
      # String(length=1) is always a palindrome
      setLRDP(right, right, True)
      # String(length=2) is a palindrome if both characters are the same
      setLRDP(right - 1, right, s[right - 1] == s[right])
      # check if the string(length=3+) is a palindrome
      for left in range(right - 2, -1, -1):
        setLRDP(left, right, LRDP[left + 1][right - 1] and s[left] == s[right])

    return count
