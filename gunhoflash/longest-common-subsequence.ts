function longestCommonSubsequence(text1: string, text2: string): number {
  const len1 = text1.length;
  const len2 = text2.length;

  // longest common subsequence's length
  const lcsl = Array(len1 + 1).fill(null).map(() => Array(len2 + 1).fill(0));

  for (let i = 1; i <= len1; i++) {
    for (let j = 1; j <= len2; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        lcsl[i][j] = lcsl[i - 1][j - 1] + 1;
      } else {
        lcsl[i][j] = Math.max(lcsl[i][j - 1], lcsl[i - 1][j]);
      }
    }
  }

  return lcsl[len1][len2];
}
