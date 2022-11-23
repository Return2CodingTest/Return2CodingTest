function countSubstrings(s: string): number {
  let count = 0;

  const L = s.length;
  const LRDP = Array(L)
    .fill(0)
    .map(() => Array(L).fill(false));

  function setLRDP(left: number, right: number, value: boolean) {
    if (value === true) {
      LRDP[left][right] = true;
      count++;
    }
  }

  // String(length=1) is always a palindrome
  setLRDP(0, 0, true);
  for (let right = 1; right < L; right++) {
    // String(length=1) is always a palindrome
    setLRDP(right, right, true);
    // String(length=2) is a palindrome if both characters are the same
    setLRDP(right - 1, right, s[right - 1] === s[right]);
    // check if the string(length=3+) is a palindrome
    for (let left = right - 2; left >= 0; left--) {
      setLRDP(left, right, LRDP[left + 1][right - 1] && s[left] === s[right]);
    }
  }

  return count;
}
