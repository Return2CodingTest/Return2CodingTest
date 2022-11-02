function minWindow(s: string, t: string): string {
  const charCountMap = new Map<string, { now: number; need: number }>();

  // init CharCount from A to Z and a to z
  for (let i = 0; i < 26; i++) {
    charCountMap.set(String.fromCharCode(65 + i), {
      now: 0,
      need: 0,
    });
    charCountMap.set(String.fromCharCode(97 + i), {
      now: 0,
      need: 0,
    });
  }

  // init need count
  for (const char of t) {
    charCountMap.get(char)!.need++;
  }

  // count the number of unsatisfied char
  let nUnsatisfiedChar = Array.from(charCountMap.values()).filter(({need}) => need > 0).length;

  let answer = '';
  let left = 0;
  for (let right = 0; right < s.length; right++) {
    const rightCharCount = charCountMap.get(s[right])!;

    rightCharCount.now++;
    if (rightCharCount.now === rightCharCount.need) {
      nUnsatisfiedChar--;
    }

    if (nUnsatisfiedChar !== 0) continue;

    // ready to shirink
    while (true) {
      const leftCharCount = charCountMap.get(s[left])!;

      // delete unnecessary char from left
      if (leftCharCount.now > leftCharCount.need) {
        leftCharCount.now--;
        left++;
      } else {
        // update answer
        if (answer.length === 0 || answer.length > right - left + 1) {
          answer = s.slice(left, right + 1);
        }
        break;
      }
    }
  }

  return answer;
}
