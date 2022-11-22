function isPalindrome(s: string): boolean {
  s = s.replace(/[^0-9A-Za-z]/g, '').toLowerCase();
  const length = s.length;
  const half = (length + 1) >> 1;
  for (let i = 0; i < half; i++) {
    if (s[i] !== s[length - 1 - i]) {
      return false;
    }
  }
  return true;
}
