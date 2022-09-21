class Letter {
  value: string;
  isUsed: boolean = false;
  before: Set<Letter> = new Set();
  after: Set<Letter> = new Set();

  constructor(value: string) {
    this.value = value;
  }
}

/**
 * convert character to number
 * @param c {string} - character
 * @returns {number} - index of character
 */
function charToInt(c: string) {
  return c.charCodeAt(0) - 97;
}

/**
 * returns first different character between two strings
 * if one string is a prefix of the other, returns null
 * @param a {string} - first word
 * @param b {string} - second word
 * @returns {string[] | null} - first different character between two strings
 */
function getFirstDiffLetters(a: string, b: string) {
  let i = 0;
  while (a[i] === b[i]) i++;
  return a[i] && b[i] ? [a[i], b[i]] : null;
}

function alienOrder(words: string[]): string {
  const letters = new Map<string, Letter>();

  Array(26).fill(0).forEach((_, i) => {
    letters.set(String.fromCharCode(i + 97), new Letter(String.fromCharCode(i + 97)));
  });

  let prevWord = '';
  for (const word of words) {
    word.split('').forEach(c => {
      letters.get(c)!.isUsed = true;
    });

    const diffLetters = getFirstDiffLetters(prevWord, word);
    if (diffLetters) {
      const [ahead, behind] = diffLetters;
      const aheadLetter = letters.get(ahead)!;
      const behindLetter = letters.get(behind)!;
      aheadLetter.after.add(behindLetter);
      behindLetter.before.add(aheadLetter);
    }

    prevWord = word;
  }

  // delete not used letters
  letters.forEach(letter => {
    if (!letter.isUsed) letters.delete(letter.value);
  });

  let answer = '';
  while (letters.size) {
    const lettersWithoutBefore = Array.from(letters.values()).filter(letter => letter.before.size === 0);
    if (lettersWithoutBefore.length === 0) break;
    lettersWithoutBefore
    .sort((a, b) => charToInt(a.value) - charToInt(b.value))
    .forEach(letter => {
      letters.delete(letter.value);
      answer += letter.value;
      letter.after.forEach(l => l.before.delete(letter));
    });
  }

  if (letters.size) return '';
  return answer;
}
