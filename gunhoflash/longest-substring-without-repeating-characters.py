class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    L = len(s)
    S = set()
    answer = 0
    left = 0
    for i in range(L):
      char = s[i]
      while char in S:
        S.remove(s[left])
        left += 1
      S.add(char)
      answer = max(answer, i - left + 1)
    return answer
