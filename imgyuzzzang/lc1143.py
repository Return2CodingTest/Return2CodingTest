#1143. Longest Common Subsequence
from collections import Counter

def longestCommonSubsequence(text1: str, text2: str) -> int:
    textDict1 = Counter(text1)
    textDict2 = Counter(text2)

    newText1 = text1
    newText2 = text2

    for k in textDict1: 
        if not k in textDict2:
            newText1.replace(k, '')
    for k in textDict2:
        if not k in textDict1:
            newText2.replace(k,'')

    n1 = len(newText1)
    n2 = len(newText2)
    
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if newText1[i-1] == newText2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n1][n2]
      