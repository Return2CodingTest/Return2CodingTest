class Solution:
  def isPalindrome(self, s: str) -> bool:
    return s == s[::-1]

  def longestPalindrome(self, s: str) -> str:
    s = '-' + s
    L = len(s)

    longestPalindromeStartIndex = 1
    longestPalindromeLength = 1

    for i in range(2, L):
      left = i - longestPalindromeLength
      right = i

      if self.isPalindrome(s[left - 1 : right + 1]):
        # 2 step longer palindrome found
        longestPalindromeStartIndex = left - 1
        longestPalindromeLength += 2
      elif self.isPalindrome(s[left : right + 1]):
        # 1 step longer palindrome found
        longestPalindromeStartIndex = left
        longestPalindromeLength += 1
    
    return s[longestPalindromeStartIndex : longestPalindromeStartIndex + longestPalindromeLength]
