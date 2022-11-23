function isPalindrome(s: string): boolean {
  const L = s.length;
  const half = (L + 1) >> 1;
  for (let i = 0; i < half; i++) {
    if (s[i] !== s[length - 1 - i]) {
      return false;
    }
  }
  return true;
}

function longestPalindrome(s: string): string {
  s = '-' + s;
  const L = s.length;

  let longestPalindromeStartIndex = 1;
  let longestPalindromeLength = 1;

  for (let i = 2; i < L; i++) {
    const left = i - longestPalindromeLength;
    const right = i;

    if (isPalindrome(s.substring(left - 1, right + 1))) {
      // 2 step longer palindrome found
      longestPalindromeStartIndex = left - 1;
      longestPalindromeLength += 2;
    } else if (isPalindrome(s.substring(left, right + 1))) {
      // 1 step longer palindrome found
      longestPalindromeStartIndex = left;
      longestPalindromeLength += 1;
    }
  }

  return s.substring(
    longestPalindromeStartIndex,
    longestPalindromeStartIndex + longestPalindromeLength
  );
}
