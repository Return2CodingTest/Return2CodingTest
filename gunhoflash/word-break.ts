function wordBreak(s: string, wordDict: string[]): boolean {
  const sLength = s.length;

  // isbreakable[i] represents that s[0:i] can be segmented into
  // a space-separated sequence of one or more dictionary words.
  const isbreakable = Array(sLength + 1).fill(false);
  isbreakable[0] = true;

  for (let i = 1; i <= sLength; i++) {
    // for each word,
    isbreakable[i] = wordDict.some(word => {
      const wordLength = word.length;
      // if s[0:i] was ended with the word,
      return (wordLength <= i && isbreakable[i - wordLength] && s.slice(i - wordLength, i) === word);
    });
  }

  return isbreakable[sLength];
}
