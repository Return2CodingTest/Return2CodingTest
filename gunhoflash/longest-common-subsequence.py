class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    len1 = len(text1)
    len2 = len(text2)

    # longest common subsequence's length
    lcsl = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
      for j in range(1, len2 + 1):
        if text1[i - 1] == text2[j - 1]:
          lcsl[i][j] = lcsl[i - 1][j - 1] + 1
        else:
          lcsl[i][j] = max(lcsl[i][j - 1], lcsl[i - 1][j])

    return lcsl[len1][len2]
