function lengthOfLongestSubstring(s: string): number {
  const L = s.length;
  const S = new Set();
  let answer = 0;
  let left = 0;
  for (let i = 0; i < L; i++) {
    const char = s[i];
    while (S.has(char)) {
      S.delete(s[left++]);
    }
    S.add(char);
    answer = Math.max(answer, i - left + 1);
  }
  return answer;
}
